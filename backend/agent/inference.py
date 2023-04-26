import numpy as np
import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
import joblib

num_path = '/home/watermelon/pgs221/BigData/Numpy'
model_path = '/home/watermelon/pgs221/BigData/Model'


for hos in os.listdir(num_path):
    print(hos)
    num_data = np.load(os.path.join(num_path, hos))

    number_data = num_data[:, :-1].astype(float)
    nan_rows = np.isnan(number_data).any(axis=1)

    # Select the rows that do not contain NaN values
    number_data_clean = number_data[~nan_rows]
    number_label_clean = num_data[:, -1][~nan_rows]
    print(number_data_clean.shape)

    # nan_indices = np.where(np.isnan(number_data))

    # # Print the indices of the NaN values
    # print(list(zip(nan_indices[0], nan_indices[1])))
    X_train, X_test, y_train, y_test = train_test_split(number_data_clean, number_label_clean, test_size=0.3, random_state=42)

    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    svm = SVC(kernel='rbf', C=1, probability=True)
    svm.fit(X_train, y_train)

    score = svm.score(X_test, y_test)
    print("Accuracy:", score)

    joblib.dump(svm, os.path.join(model_path, hos + '.joblib'))

    # exit(0)