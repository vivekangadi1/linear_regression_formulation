import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

X = []
Y = []

for line in open('inear_regression_formulation\data_2d.csv'):
    x1,x2,y = line.split(',')
    X.append([float(x1),float(x2),1])
    Y.append(float(y))


# fig = plt.figure()
# ax = fig.add_subplot(111,projection='3d')
# ax.scatter(X[:,0], X[:,1], Y)
# plt.show()
X = np.array(X)
Y = np.array(Y)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X[:,0], X[:,1], Y)
plt.show()


w = np.linalg.solve(np.dot(X.T,X),np.dot(X.T,Y))

Yhat = np.dot(X,w)

d1 = Y - Yhat
d2 = Y - Y.mean()
r2 = 1 - d1.dot(d1) / d2.dot(d2)
print("the r-squared is:", r2)