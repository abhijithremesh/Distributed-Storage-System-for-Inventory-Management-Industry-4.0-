import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
import pickle

df=pd.read_csv("C:\\Distributed Storage System\log.csv")
df.columns = ['timestamp', 'scale_id', 'article','unit_weight', 'obtained_weight','count']
df = df[df.obtained_weight != 0]
df = df.drop([ 'scale_id','timestamp','unit_weight','count'], axis=1)
df = df[['obtained_weight', 'article']]
feature_names = ['obtained_weight']
X = df[feature_names]
y = df['article']

#splitting into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

#scaling the train and test
scaler = MinMaxScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

#training decison tree classifier
clf = DecisionTreeClassifier().fit(X_train, y_train)
print('Accuracy of Decision Tree classifier on training set: {:.2f}'
     .format(clf.score(X_train, y_train)))
print('Accuracy of Decision Tree classifier on test set: {:.2f}'
     .format(clf.score(X_test, y_test)))

#training knn model
knn = KNeighborsClassifier()
knn.fit(X_train, y_train)
print('Accuracy of K-NN classifier on training set: {:.2f}'
     .format(knn.score(X_train, y_train)))
print('Accuracy of K-NN classifier on test set: {:.2f}'
     .format(knn.score(X_test, y_test)))

# save the model 
filepath = r'C:\Distributed Storage System\dtc.pckl'
pickle.dump(clf, open(filepath, 'wb'))

filepath = r'C:\Distributed Storage System\knnc.pckl'
pickle.dump(knn, open(filepath, 'wb'))

