from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
import numpy as np
import io

model = load_model('CNN_ECG.h5')
NUM_TIMESTEPS = 5000

def load_data(filename):
    # Load data from file
    data = np.genfromtxt(filename, delimiter=' ')
    return data

def preprocess_data(data):
    # Load data from file
    # Preprocess data
    X = np.zeros((1, NUM_TIMESTEPS, 8))
    X[0] = data
    X = np.expand_dims(X, axis=-1)
    X = np.reshape(X, (X.shape[0], X.shape[2], X.shape[1], 1))
    return X

data = load_data('110835.asc')
input = preprocess_data(data)
y_pred = model.predict(input)
label_dict = {0: "Normal ECG", 1: "Abnormal ECG", 2: "Otherwise normal ECG", 3: "Borderline ECG"}

app = Flask(__name__)

@app.route('/CNN', methods=['POST'])
def predict_ecg():
    file = request.files['file']
    raw_data = file.read()
    raw_data = np.fromstring(raw_data, sep='\n').reshape((5000, 8))
    data = preprocess_data(raw_data)
    y_pred = model.predict(data)
    label = label_dict[np.argmax(y_pred, axis=1)[0]]
    return jsonify({'label': label})

if __name__ == '__main__':
    app.run(debug=True)
