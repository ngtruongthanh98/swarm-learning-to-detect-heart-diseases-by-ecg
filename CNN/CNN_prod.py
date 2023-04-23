from tensorflow.keras.models import load_model
import numpy as np

model = load_model('CNN_ECG.h5')
NUM_TIMESTEPS = 5000

def load_data(filename):
    # Load data from file
    data = np.genfromtxt(filename, delimiter=' ')
    return data

def preprocess_data(filename):
    # Load data from file
    data = load_data(filename)
    # Preprocess data
    X = np.zeros((1, NUM_TIMESTEPS, 8))
    X[0] = data
    X = np.expand_dims(X, axis=-1)
    X = np.reshape(X, (X.shape[0], X.shape[2], X.shape[1], 1))
    return X

input = preprocess_data("pulse2pulse_150k/from_006_chkp_2500_150k/100000.asc")
y_pred = model.predict(input)
label_dict = {0: "Normal ECG", 1: "Abnormal ECG", 2: "Otherwise normal ECG", 3: "Borderline ECG"}

print(label_dict[np.argmax(y_pred, axis=1)[0]])