import pandas as pd
import numpy as np
import os
from scipy.signal import find_peaks
import peakutils

num_path = '/home/watermelon/pgs221/BigData/Numpy'
df = pd.read_csv('/home/watermelon/pgs221/BigData/Dataset/Deepfake-ecg/pulse2pulse_150k_ground_truth.csv', sep=';')
null_cols = df.columns[df.isnull().any()]

# print(df.columns.tolist())
# TestID = df['patid']
# sample = df[df['patid'] == 14888]

# print(sample['tonset'].values[0] + 1)

def file_is_hidden(p):
    return p.startswith('.')

def get_hrv(lead):
    threshold = 0.5 * np.max(lead)

    # Find R peaks using the find_peaks function
    r_peak_indices, _ = find_peaks(lead, height=threshold, distance=500)

    print(lead[r_peak_indices])
    # Calculate RR intervals
    rr_intervals = np.diff(r_peak_indices)

    print('Rate: ', rr_intervals)

    qrs_inds = peakutils.indexes(lead, thres=0.5, min_dist=500)

    # Define window size for R-peak amplitude extraction
    win_size = int(0.025 * 1000)  # assuming sampling rate of 1000 Hz

    # Extract R-peak amplitudes
    r_peak_ampli = []
    for r in qrs_inds:
        r_peak_ampli.append(np.max(ecg[r-win_size:r+win_size]))

    print(r_peak_ampli)

    qrs_durations = []
    for i in range(len(r_peak_indices)):
        r_peak_index = r_peak_indices[i]
        q_point_index = np.argmin(lead[r_peak_index:r_peak_index+50]) + r_peak_index
        s_point_index = np.argmin(lead[r_peak_index:r_peak_index+100]) + r_peak_index

        qrs_duration = s_point_index - q_point_index
        qrs_durations.append(qrs_duration)

    # Calculate HRV as the standard deviation of the RR intervals
    hrv = np.std(rr_intervals)
    qrs_complex = np.mean(qrs_durations)
    return hrv, qrs_complex

split_path = "/home/watermelon/pgs221/BigData/Hospitals"
hospitals = ["ChoRay", "BachMai", "TamDuc", "VietPhap", "115People"]

# [numqrs, ventrate, atrialrate, r_peak{i-v6}, t_peak{i-v6}, p_peak{i-v6}, t_duration{i-v6}, p_duration{i-v6}, ecg_class]


for hos in hospitals:

    result = np.array([np.zeros((44, ))])
    print(hos)
    ecgs_path = os.path.join(split_path, hos)
    ecgs_files = [f for f in os.listdir(ecgs_path) if not file_is_hidden(f)]
    for file in ecgs_files:
        # print(file)
        res = np.array([])
        # ecg = np.loadtxt(os.path.join(split_path, hos, file))
        name_without_ext = os.path.splitext(file)[0]
        # print(name_without_ext)
        ecg = df[df['patid'] == int(name_without_ext)]

        res = np.append(res, ecg['NumQRSComplexes'].values[0])    
        res = np.append(res, ecg['VentRate'].values[0])    
        res = np.append(res, ecg['AtrialRate'].values[0])    

        res = np.append(res, ecg.loc[:, 'R_PeakAmpl_i' : 'R_PeakAmpl_v6'].values[0])  
        res = np.append(res, ecg.loc[:, 'T_PeakAmpl_i' : 'T_PeakAmpl_v6'].values[0])  
        res = np.append(res, ecg.loc[:, 'P_PeakAmpl_i' : 'P_PeakAmpl_v6'].values[0])  
        

        res = np.append(res, ecg.loc[:, 'T_Duration_i' : 'T_Duration_v6'].values[0])  
        res = np.append(res, ecg.loc[:, 'P_Duration_i' : 'P_Duration_v6'].values[0])  

        res = np.append(res, ecg['ecgcategory'].values[0])    
        result = np.vstack((result, res))

    result = result[1:]
    np.save(os.path.join(num_path, hos + '.npy'), result)