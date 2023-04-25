import numpy as np
from tensorflow.keras.models import load_model
from sklearn.metrics import confusion_matrix
import os
os.environ['CUDA_VISIBLE_DEVICES'] = ''

# Load validation data
data_val = np.load('data_valid.npz')
X_val, y_val = data_val['X'], data_val['y']

# Load saved model
model = load_model('CNN_ECG.h5')

# Make predictions on validation set
y_pred = model.predict(X_val)

# Calculate confusion matrix
cm = confusion_matrix(np.argmax(y_val, axis=1), np.argmax(y_pred, axis=1))
print(cm)

total_samples = np.sum(cm)
correct_predictions = np.sum(np.diag(cm))

accuracy = correct_predictions / total_samples
print("Accuracy:", accuracy)

recall = np.zeros(4)
for i in range(4):
    tp = cm[i,i]
    fn = np.sum(cm[i,:]) - tp
    recall[i] = tp / (tp + fn)
    
print("Recall:", recall)
