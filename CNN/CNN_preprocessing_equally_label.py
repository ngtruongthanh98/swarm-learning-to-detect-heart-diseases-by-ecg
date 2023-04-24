import numpy as np
import pandas as pd
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.layers import Reshape, Flatten, Input, Dense, Embedding, Conv2D, MaxPooling2D, Dropout, concatenate
from tensorflow.keras import regularizers
from tensorflow.keras.models import Model
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.optimizers import Adam
from sklearn.metrics import confusion_matrix

# Define constants
NUM_SAMPLES = 18000
NUM_TIMESTEPS = 5000
NUM_CLASSES = 4
EMBEDDING_DIM = 8

# Define function to load data from .asc files
def load_data(filename):
    # Load data from file
    data = np.genfromtxt(filename, delimiter=' ')
    return data

def preprocess_data_and_labels(selected_samples, labels):
    # Initialize arrays for data and labels
    X = np.zeros((len(selected_samples), NUM_TIMESTEPS, 8))
    y = np.zeros((len(selected_samples), NUM_CLASSES))
    # Loop over selected samples and corresponding labels
    for i, (selected_samples, label) in enumerate(zip(selected_samples, labels)):
        # Add data to X array
        X[i] = selected_samples
        # Convert label to one-hot encoding and add to y array
        y[i] = to_categorical(label, num_classes=NUM_CLASSES)
    X = np.expand_dims(X, axis=-1)
    X = np.reshape(X, (X.shape[0], X.shape[2], X.shape[1], 1))
    return X, y

# Load csv file with labels
labels_df = pd.read_csv('.csv', sep=';')

# Create a dictionary to map class labels to indices
label_dict = {"Normal ECG": 0, "Abnormal ECG": 1, "Otherwise normal ECG": 2, "Borderline ECG": 3}

# Create empty arrays to store selected samples and their labels
selected_samples = []
selected_labels = []
pulse2pulse_150k_ground_truth
# Loop over each class label
for label in label_dict:
    # Get indices of samples with current label
    indices = labels_df.loc[labels_df['ecgcategory'] == label]['patid'].values
    # Randomly select 18000 samples from the current label's indices
    selected_indices = np.random.choice(indices, size=18000//len(label_dict), replace=False)
    # Load and preprocess the selected samples
    for patid in selected_indices:
        filename = 'pulse2pulse_150k/from_006_chkp_2500_150k/{}.asc'.format(patid)
        data = load_data(filename)
        selected_samples.append(data)
        selected_labels.append(label_dict[label])

# Convert selected samples and labels to numpy arrays
selected_samples = np.array(selected_samples)
selected_labels = np.array(selected_labels)
print("🚀 ~ file: CNN_preprocessing.py:67 ~ selected_labels:", selected_labels)

# Preprocess selected samples and labels
X, y = preprocess_data_and_labels(selected_samples, selected_labels)
print('X', X.shape)
np.savez('preprocessed_data.npz', X=X, y=y)
