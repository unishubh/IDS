import sklearn
from sklearn.externals import joblib
import pandas
from sklearn.cross_validation import train_test_split
from time import time
from sklearn.preprocessing import MinMaxScaler
import csv
import pickle


##---Shukla----

def perf_measure(y_actual, y_hat,leng):
    TP = 0.0
    FP = 0.0
    TN = 0.0
    FN = 0.0

    '''for i in range(len(y_hat)): 
        if y_actual[i]==y_hat[i]=='attack':
           TP += 1
    for i in range(len(y_hat)): 
        if y_hat[i]=='attack' and y_actual!=y_hat[i]:
           FP += 1
    for i in range(len(y_hat)): 
        if y_actual[i]==y_hat[i]=='normal':
           TN += 1
    for i in range(len(y_hat)): 
        if y_hat[i]=='normal' and y_actual!=y_hat[i]:
           FN += 1
    '''
    for i in range (len(y_hat)):
    #  print "The state is",y_hat[i]
      if y_hat[i] == 'attack.':
	# print "attack detected"
         if y_hat[i] == y_actual.iloc[i]:
            TP +=1
         else:
            TN += 1
      else:
        #  print "normal detection"
          if y_hat[i] == y_actual.iloc[i]:
            FN +=1
          else:
            FP += 1
    print TP,TN,FP,FN
    print "The false negative rate is",float(FN/leng)
    


##---Shukla--##



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

features_train, features_test, labels_train, labels_test = train_test_split(
    kdd_data_corrected[num_features], 
    kdd_data_corrected['label'], 
    test_size=0.1, 
    random_state=42)
instance=[[0,'udp','private','SF',105,146,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0.00,0.00,0.00,0.00,1.00,0.00,0.00,255,254,1.00,0.01,0.00,0.00,0.00,0.00,0.00,0.0
]]
t0 = time()
clf=joblib.load('model/clf.pkl')
print "success load"
pred = clf.predict(features_test[0:31103])

with open('names.csv', 'w') as csvfile:
    fieldnames = ['Decision']
    writer = csv.writer(csvfile)
    for i in pred:
	#print i
        writer.writerow([i]) 

print "success predict"
tt = time() - t0
print "Predicted in {} seconds".format(round(tt,31103))
#print pred

##----Shukla's Code---
#print "The labels were"
#print labels_test[0:10000]

print len(pred)
print len(labels_test)

perf_measure(labels_test[0:31103], pred,31103)

"""
from sklearn.metrics import accuracy_score
acc = accuracy_score(labels_test, pred)
print "R squared is {}.".format(round(acc,4))
"""
