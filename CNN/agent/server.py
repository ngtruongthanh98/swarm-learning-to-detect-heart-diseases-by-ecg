import os
import joblib
import pandas as pd
import numpy as np

model_path = '/home/watermelon/pgs221/BigData/source/swarm-learning-to-detect-heart-diseases-by-ecg/CNN/agent/models_prob'
hospital_ids = {0: 'Swarm', 1: 'ChoRay', 2: 'BachMai', 3: 'TamDuc', 4: 'VietPhap', 5: '115People'}
ecg_data = pd.read_csv('/home/watermelon/pgs221/BigData/Dataset/Deepfake-ecg/pulse2pulse_150k_ground_truth.csv', sep=';')

df = pd.read_csv('/home/watermelon/pgs221/BigData/Dataset/Deepfake-ecg/pulse2pulse_150k_ground_truth.csv', sep=';')
# class_names = ['Normal ECG', 'Abnormal ECG', 'Borderline ECG', 'Otherwise normal ECG']



def GetInfoByHositalAndID(hospital, id):
    print('GetInfoByHositalAndID: ', hospital, id)
    hospital_model = joblib.load(os.path.join(model_path, hospital_ids[hospital] + '.npy.joblib'))

    res = np.array([])
    # ecg = np.loadtxt(os.path.join(split_path, hos, file))
    # print(name_without_ext)
    ecg = df[df['patid'] == int(id)]
    res = np.append(res, ecg['NumQRSComplexes'].values[0])    
    res = np.append(res, ecg['VentRate'].values[0])    
    res = np.append(res, ecg['AtrialRate'].values[0])    
    res = np.append(res, ecg.loc[:, 'R_PeakAmpl_i' : 'R_PeakAmpl_v6'].values[0])  
    res = np.append(res, ecg.loc[:, 'T_PeakAmpl_i' : 'T_PeakAmpl_v6'].values[0])  
    res = np.append(res, ecg.loc[:, 'P_PeakAmpl_i' : 'P_PeakAmpl_v6'].values[0])  
    
    res = np.append(res, ecg.loc[:, 'T_Duration_i' : 'T_Duration_v6'].values[0])  
    res = np.append(res, ecg.loc[:, 'P_Duration_i' : 'P_Duration_v6'].values[0])  
    res = np.append(res, ecg['ecgcategory'].values[0])

    probs = hospital_model.predict_proba([res[:-1]])
    print(probs)
    # percentages = (probs.sum(axis=0)/len(res[:-1]))*100
    percentages = probs[0]

    # Get label names and their corresponding percentages
    results = {}
    class_names = hospital_model.classes_
    for idx, class_name in enumerate(class_names):
        percentage = percentages[idx]
        results[class_name] = percentage


    print('RES: ', results)

    return results