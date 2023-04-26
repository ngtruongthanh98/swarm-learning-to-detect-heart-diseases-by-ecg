import numpy as np
import pandas as pd
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.layers import Reshape, Flatten, Input, Dense, Embedding, Conv2D, MaxPooling2D, Dropout, concatenate
from tensorflow.keras import regularizers
from tensorflow.keras.models import Model
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.optimizers import Adam
from sklearn.metrics import confusion_matrix

import os
from tensorflow.keras.callbacks import ModelCheckpoint

# Define constants
NUM_TIMESTEPS = 5000
NUM_CLASSES = 4
EMBEDDING_DIM = 8

data = np.load('shuffle_data.npz')
X = data['X']
print("🚀 ~ file: CNN.py:22 ~ X:", X.shape)
y = data['y']
NUM_SAMPLES = len(y)
print("🚀 ~ file: CNN.py:23 ~ y:", y[:30])

# Split data into training and validation sets
split_idx = int(0.95 * NUM_SAMPLES)
X_train, y_train = X[:split_idx], y[:split_idx]
X_val, y_val = X[split_idx:], y[split_idx:]
print("🚀 ~ file: CNN.py:28 ~ y_train:", y_train.shape)
print("🚀 ~ file: CNN.py:29 ~ y_val:", y_val.shape)

np.savez('data_valid.npz', X=X_val, y=y_val)

# lead 8 for the second dim, None is the third dim (the length of sequence), and 1 is channel
inputs = Input(shape=(EMBEDDING_DIM, NUM_TIMESTEPS, 1))
filter_sizes = [5, 6, 7]
num_filters = 32

drop = 0.5

conv_0 = Conv2D(num_filters, (filter_sizes[0], EMBEDDING_DIM),
                activation='relu', kernel_regularizer=regularizers.l2(0.01), data_format="channels_last")(inputs)
conv_1 = Conv2D(num_filters, (filter_sizes[1], EMBEDDING_DIM),
                activation='relu', kernel_regularizer=regularizers.l2(0.01), data_format="channels_last")(inputs)
conv_2 = Conv2D(num_filters, (filter_sizes[2], EMBEDDING_DIM),
                activation='relu', kernel_regularizer=regularizers.l2(0.01), data_format="channels_last")(inputs)

maxpool_0 = MaxPooling2D(
    (EMBEDDING_DIM - filter_sizes[0] + 1, 1), strides=(1, 1))(conv_0)
maxpool_1 = MaxPooling2D(
    (EMBEDDING_DIM - filter_sizes[1] + 1, 1), strides=(1, 1))(conv_1)
maxpool_2 = MaxPooling2D(
    (EMBEDDING_DIM - filter_sizes[2] + 1, 1), strides=(1, 1))(conv_2)

merged_tensor = concatenate([maxpool_0, maxpool_1, maxpool_2], axis=1)
flatten = Flatten()(merged_tensor)
dropout = Dropout(drop)(flatten)
output = Dense(units=4, activation='softmax',
               kernel_regularizer=regularizers.l2(0.01))(dropout)


# this creates a model that includes
model = Model(inputs, output)


adam = Adam(lr=0.001, beta_1=0.9, beta_2=0.999, epsilon=1e-08)
model.compile(loss='categorical_crossentropy', optimizer=adam, metrics=['accuracy'])
model.summary()

# define callbacks
early_stopping = EarlyStopping(
    monitor='val_loss', min_delta=0.01, patience=4, verbose=1)
callbacks_list = [early_stopping]



# define callbacks
checkpoint_path = "model_checkpoint.h5"
checkpoint_dir = os.path.dirname(checkpoint_path)
checkpoint_callback = ModelCheckpoint(
    checkpoint_path, 
    save_weights_only=True,
    monitor='val_loss',
    mode='min',
    save_best_only=True,
    save_freq=1 # save every 5 epochs
)


model.fit(X_train, y_train, validation_split=0.1,
          epochs=10, batch_size=16, callbacks=callbacks_list, shuffle=True, verbose=2)

# save the model to disk
model.save("CNN_ECG.h5")

y_pred = model.predict(X_val)
y_pred_classes = np.argmax(y_pred, axis=1)
y_true = np.argmax(y_val, axis=1)

confusion_mtx = confusion_matrix(y_true, y_pred_classes)
print("🚀 ~ file: CNN.py:130 ~ confusion_mtx:", confusion_mtx)
