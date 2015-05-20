%matplotlib inline
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import csv
from sklearn import preprocessing 
import numpy as np

X = []
with open ('combinedmatrix.CSV') as f:
    reader = csv.reader(f)
    for row in reader:
        r = [float(x) for x in row]
        X.append(r)
        
X = np.array(X)
X = X[:,50:263]
print X.shape

Xcentered = preprocessing.scale(X)
pca = PCA()
p = pca.fit(Xcentered)

# first visualize the explained variance
W = p.components_
plt.plot(p.explained_variance_ratio_)
plt.show

#just to check variance 
np.sum(p.explained_variance_ratio_[0:180])

# choose L principal components
#Z = np.dot(Xcentered.transpose(),W[0:L,:])

# Z – data in reduced space
