from sklearn.externals import joblib
import pandas
from sklearn.cross_validation import train_test_split
from time import time
from sklearn.preprocessing import MinMaxScaler
import csv

col_names = ["duration","protocol_type","service","flag","src_bytes",
    "dst_bytes","land","wrong_fragment","urgent","hot","num_failed_logins",
    "logged_in","num_compromised","root_shell","su_attempted","num_root",
    "num_file_creations","num_shells","num_access_files","num_outbound_cmds",
    "is_host_login","is_guest_login","count","srv_count","serror_rate",
    "srv_serror_rate","rerror_rate","srv_rerror_rate","same_srv_rate",
    "diff_srv_rate","srv_diff_host_rate","dst_host_count","dst_host_srv_count",
    "dst_host_same_srv_rate","dst_host_diff_srv_rate","dst_host_same_src_port_rate",
    "dst_host_srv_diff_host_rate","dst_host_serror_rate","dst_host_srv_serror_rate",
    "dst_host_rerror_rate","dst_host_srv_rerror_rate","label"]
num_features = [
    "duration","src_bytes",
    "dst_bytes","land","wrong_fragment","urgent","hot","num_failed_logins",
    "logged_in","num_compromised","root_shell","su_attempted","num_root",
    "num_file_creations","num_shells","num_access_files","num_outbound_cmds",
    "is_host_login","is_guest_login","count","srv_count","serror_rate",
    "srv_serror_rate","rerror_rate","srv_rerror_rate","same_srv_rate",
    "diff_srv_rate","srv_diff_host_rate","dst_host_count","dst_host_srv_count",
    "dst_host_same_srv_rate","dst_host_diff_srv_rate","dst_host_same_src_port_rate",
    "dst_host_srv_diff_host_rate","dst_host_serror_rate","dst_host_srv_serror_rate",
    "dst_host_rerror_rate","dst_host_srv_rerror_rate"
]




kdd_data_corrected = pandas.read_csv("corrected", header=None, names = col_names)
kdd_data_corrected['label'].value_counts()
print "success read "

kdd_data_corrected['label'][kdd_data_corrected['label']!='normal.'] = 'attack.'
print kdd_data_corrected['label'].value_counts()

from sklearn.cross_validation import train_test_split
kdd_data_corrected[num_features] = kdd_data_corrected[num_features].astype(float)
kdd_data_corrected[num_features].apply(lambda x: MinMaxScaler())
print "success normailized"

t0 = time()
km=joblib.load('model2/km.pkl')
pred = km.predict(kdd_data_corrected[num_features])
tt = time() - t0
with open('names2.csv', 'w') as csvfile:
    fieldnames = ['Decision']
    writer = csv.writer(csvfile)
    for i in pred:
	print i
        writer.writerow([i]) 
print "Assigned clusters in {} seconds".format(round(tt,3))
print pred
