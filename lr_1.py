import numpy as np
import matplotlib.pyplot as plt

X=[]
Y=[]
for line in open('data_1d.csv'):
    x,y = line.split(',')
    X.append(float(x))
    Y.append(float(y))

X= np.array(X)
Y = np.array(Y)

denominator = X.dot(X) - X.mean()*X.sum()
a = (X.dot(Y) - Y.mean()*X.sum()) / denominator
b = (Y.mean()*X.dot(X) - X.mean()*X.dot(Y)) /denominator

y1 = a*(X) + b
plt.scatter(X,Y)
plt.plot(X,y1)
plt.show()

d1 = Y - y1
d2 = Y - Y.mean()

r2 = 1 - d1.dot(d1)/d2.dot(d2)

print(r2)