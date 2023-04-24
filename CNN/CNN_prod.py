from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
import numpy as np
import json

model1 = load_model('CNN_ECG.h5')
model2 = load_model("choray_CNN_ECG.h5")

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
y_pred = model1.predict(input)
label_dict = {0: "Normal ECG", 1: "Abnormal ECG", 2: "Otherwise normal ECG", 3: "Borderline ECG"}

app = Flask(__name__)

@app.route('/result/<int:hospital_id>', methods=['POST'])
def predict_ecg(hospital_id):
    if hospital_id == 1:
        model = model1
    elif hospital_id == 2:
        model = model2
    raw_data = request.data
    raw_data = np.fromstring(raw_data, sep='\n').reshape((5000, 8))
    data = preprocess_data(raw_data)
    y_pred = model.predict(data)
    normalized_predict = [(val/sum(y_pred[0]))*100 for val in y_pred[0]]

    # create a list of dictionaries with the label and percentage values
    result = [{'title': label_dict[i], 'value': percent} for i, percent in enumerate(normalized_predict)]

    # convert the list to a JSON object
    json_result = json.dumps(result)
    return json_result

if __name__ == '__main__':
    app.run(debug=True)
