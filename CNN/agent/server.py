from flask import Flask, request, jsonify
import joblib
import os


app = Flask(__name__)
model_path = '/home/watermelon/pgs221/BigData/source/swarm-learning-to-detect-heart-diseases-by-ecg/agent/models'
hospital_ids = {0: 'Swarm', 1: 'ChoRay', 2: 'BachMai', 3: 'TamDuc', 4: 'VietPhap', 5: '115People'}

@app.route('/result/svm/<int:hospital_id>', methods=['POST'])
def predict_ecg(hospital_id):
    print('?')
    file_name = os.path.join(model_path, hospital_ids[hospital_id] + '.npy.joblib')
    model = joblib.load(file_name)


if __name__ == '__main__':
    app.run(debug=True)