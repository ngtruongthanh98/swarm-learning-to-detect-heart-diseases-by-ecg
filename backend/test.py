import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix
from sklearn import preprocessing


df = pd.read_csv("Deepfake-ecg/pulse2pulse_150k_ground_truth.csv", sep=';')

print(df['patid'])
drop_list = ['TestID', 'patid', 'AcquisitionDateTime_DT', 'AnalysisSoftwareVersion', 'ecgday', 'sl_19',
'sl_21',
'sl_22',
'sl_23',
'sl_24',
'sl_32',
'sl_33',
'sl_42',
'sl_43',
'sl_61',
'sl_62',
'sl_101',
'sl_102',
'sl_103',
'sl_104',
'sl_105',
'sl_107',
'sl_108',
'sl_141',
'sl_142',
'sl_143',
'sl_144',
'sl_161',
'sl_162',
'sl_171',
'sl_174',
'sl_175',
'sl_177',
'sl_178',
'sl_179',
'sl_181',
'sl_184',
'sl_211',
'sl_212',
'sl_221',
'sl_222',
'sl_231',
'sl_233',
'sl_234',
'sl_235',
'sl_237',
'sl_242',
'sl_243',
'sl_244',
'sl_245',
'sl_246',
'sl_247',
'sl_251',
'sl_252',
'sl_267',
'sl_271',
'sl_299',
'sl_302',
'sl_304',
'sl_350',
'sl_360',
'sl_369',
'sl_372',
'sl_380',
'sl_383',
'sl_384',
'sl_390',
'sl_410',
'sl_411',
'sl_440',
'sl_445',
'sl_450',
'sl_465',
'sl_470',
'sl_471',
'sl_482',
'sl_487',
'sl_520',
'sl_540',
'sl_541',
'sl_542',
'sl_543',
'sl_544',
'sl_545',
'sl_548',
'sl_700',
'sl_740',
'sl_760',
'sl_780',
'sl_801',
'sl_802',
'sl_803',
'sl_806',
'sl_810',
'sl_820',
'sl_821',
'sl_830',
'sl_831',
'sl_900',
'sl_901',
'sl_902',
'sl_903',
'sl_930',
'sl_940',
'sl_950',
'sl_961',
'sl_963',
'sl_964',
'sl_965',
'sl_966',
'sl_967',
'sl_1000',
'sl_1001',
'sl_1002',
'sl_1024',
'sl_1070',
'sl_1100',
'sl_1140',
'sl_1141',
'sl_1142',
'sl_1143',
'sl_1150',
'sl_1170',
'sl_1180',
'sl_1672',
'sl_1680',
'sl_1682',
'sl_1684',
'sl_1687',
'sl_1693',
'sl_1699',
'numcodes',]

df = df.drop(drop_list,axis=1)
df.dropna(inplace=True)

#test train split time
from sklearn.model_selection import train_test_split

print('categories:', df['ecgcategory'].unique())
y = preprocessing.LabelEncoder().fit_transform(df['ecgcategory'].values)

X = df.drop(['ecgcategory'],axis=1).values #features
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,
                                            random_state=42, stratify=y)

from sklearn.naive_bayes import GaussianNB
clf = GaussianNB()
# fit it to training data
clf.fit(X_train,y_train)
# predict using test data
y_pred = clf.predict(X_test)

train_pred = clf.predict(X_train)

cm = confusion_matrix(y_test,y_pred)
print('test-set confusion matrix:\n', cm) 

#compute tp, tp_and_fn and tp_and_fp w.r.t all classes
tp_and_fn = cm.sum(1)
tp_and_fp = cm.sum(0)
tp = cm.diagonal()
print("tp:", tp)

precision = tp / tp_and_fp
print("precision:", precision)
recall = tp / tp_and_fn
print("recall:", recall)

