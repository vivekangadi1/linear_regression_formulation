import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

X = []
Y = []

for line in open('data_2d.csv'):
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
