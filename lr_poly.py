import numpy as np
import matplotlib.pyplot as plt

X = []
Y = []

for line in open('data_poly.csv'):
     x,y = line.split(',')
     x = float(x)
     X.append([1,x,x*x])
     Y.append(float(y))

X = np.array(X)
Y = np.array(Y)

plt.scatter(X[:,1],Y)
plt.title('scatter data')
plt.show()


w = np.linalg.solve(np.dot(X.T,X),np.dot(X.T,Y))


plt.scatter(X[:,1], Y)
Yhat = X.dot(w)

#plotting the fitted line
plt.scatter(X[:,1],Yhat)
plt.title('predicted data')
plt.show()


d1 = Y - Yhat
d2 = Y - Y.mean()

r = 1 - d1.dot(d1)/d2.dot(d2)
print("the r2 value",r2)
