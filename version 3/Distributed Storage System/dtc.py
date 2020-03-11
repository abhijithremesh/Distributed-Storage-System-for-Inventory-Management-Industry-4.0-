from numpy import array
import sys
import json
import pandas as pd
import pickle
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

data = sys.argv[1]
data = json.loads(data)

obw = data['obtainedweight']
cnt = data['count']

filepath = r'C:\Distributed Storage System\dtc.pckl'
decisiontree = pickle.load(open(filepath, 'rb'))

df=pd.read_csv("C:\\Distributed Storage System\log.csv")
df.columns = ['timestamp', 'scale_id', 'article','unit_weight', 'obtained_weight','count']
df = df[df.obtained_weight != 0]
df = df.drop([ 'scale_id','timestamp','unit_weight'], axis=1)
df = df[['obtained_weight','count', 'article']]
feature_names = ['obtained_weight','count']
X = df[feature_names]
y=df['article']

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

scaler = MinMaxScaler()
X_train = scaler.fit_transform(X_train)

parameters = array([obw,cnt])
parameters = parameters.reshape(1,-1)

X_test = scaler.transform(parameters)


print(decisiontree.predict(X_test))