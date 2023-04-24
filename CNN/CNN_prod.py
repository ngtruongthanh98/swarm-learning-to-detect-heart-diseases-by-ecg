from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
import numpy as np
import json
from flask_cors import CORS
from agent.server import GetInfoByHositalAndID
import math
import os

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
CORS(app)

@app.route('/result/cnn/<int:hospital_id>', methods=['POST'])
def predict_ecg(hospital_id):
    if hospital_id == 1:
        model = model1
    elif hospital_id == 2:
        model = model2
    # elif hospital_id == 3:
    #     model = model1
    # elif hospital_id == 4:
    #     model = model2
    # elif hospital_id == 5:
    #     model = model1

    json_data = request.get_json()
    raw_data = json_data["body"]["data"]
    print("🚀 ~ file: CNN_prod.py:42 ~ raw_data:", raw_data)
    raw_data = np.fromstring(raw_data, sep=' ').reshape((5000, 8))
    data = preprocess_data(raw_data)
    y_pred = model.predict(data)
    normalized_predict = [(val/sum(y_pred[0]))*100 for val in y_pred[0]]
    rounded_predict = list(map(lambda x: round(x, 2), normalized_predict))

    # create a list of dictionaries with the label and percentage values
    result = [{'title': label_dict[i], 'value': percent} for i, percent in enumerate(rounded_predict)]

    # convert the list to a JSON object
    json_result = json.dumps(result)
    return json_result

@app.route('/result/svm/<int:hospital_id>', methods=['POST'])
def predict_svm_ecg(hospital_id):
    if hospital_id == 1:
        model = model1
    elif hospital_id == 2:
        model = model2
    json_data = request.get_json()
    file_name = json_data["body"]["data"]
    print("🚀 ~ file: CNN_prod.py:42 ~ file_name:", file_name)
    
    res = GetInfoByHositalAndID(hospital_id, os.path.splitext(file_name)[0])

    # create a list of dictionaries with the label and percentage values
    result = [{'title': key, 'value': round(res[key] * 100, 2)} for key in res]

    # convert the list to a JSON object
    json_result = json.dumps(result)
    return json_result

if __name__ == '__main__':
    app.run(debug=True)
