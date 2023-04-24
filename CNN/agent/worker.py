import numpy as np
import os
import shutil
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

path = "/home/watermelon/pgs221/BigData/Dataset/Deepfake-ecg/pulse2pulse_150k/from_006_chkp_2500_150k"
split_path = "/home/watermelon/pgs221/BigData/Hospitals"
hospitals = ["ChoRay", "BachMai", "TamDuc", "VietPhap", "115People"]


# def file_is_hidden(p):
#     return p.startswith('.')

# ecg_files = [f for f in os.listdir(path) if not file_is_hidden(f)]
# # ec_len = len(ec_files)
# # split_ec_files = np.split(ec_files, [int(0.8 * ec_len), int(0.9 * ec_len)])
# # train_ec_files = split_ec_files[0]
# # validation_ec_files = split_ec_files[1]
# # test_ec_files = split_ec_files[2]
# print(len(ecg_files))
# print(ecg_files[0])

# ec_len = len(ecg_files)
# split_ecg_files = np.split(ecg_files, [int(0.2 * ec_len), int(0.4 * ec_len), int(0.6 * ec_len), int(0.8 * ec_len)])
# print("Number of split ecg files", len(split_ecg_files))
# i = 0
# for hospital in hospitals:
#     save_path = os.path.join(split_path, hospital)

#     for k in split_ecg_files[i]:
#         src_path = os.path.join(path, k)
#         des_path = os.path.join(save_path, k)
#         shutil.copy2(src_path, des_path)

#     print("Hospital: ", hospital, " has total ", len(split_ecg_files[i]), " sample")
#     i = i + 1

