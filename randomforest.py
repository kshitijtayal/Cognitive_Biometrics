from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np
from numpy import genfromtxt,savetxt
from sklearn import preprocessing 

dataset = genfromtxt(open('multi.txt','r'),delimiter = ',')

Y =  dataset[:,213]   #target
X = dataset[:,0:212]

s = np.random.permutation(len(Y))
n = 0.80*dataset.shape[0]
trainX = X[s[0:n],:]
trainY = Y[s[0:n]]   #train target
testX = X[s[n:],:]
testY = Y[s[n:]]    #test target
print trainX.shape
print testX.shape


Xcentered = preprocessing.scale(trainX)
test_centered = preprocessing.scale(testX)

rf = RandomForestClassifier(n_estimators=200, n_jobs=4)
rf.fit(trainX, trainY)
preds = rf.predict(testX)

 savetxt('submission3.csv', pd.crosstab(testY, preds, rownames=['actual'], colnames=['preds']), delimiter=',', fmt='%f')
 m = genfromtxt(open('submission2.csv','r'),delimiter = ',')
count = 0
for i in xrange(0, len(m)):
    count += m[i][i]
print count
print count/(testX.shape[0])
