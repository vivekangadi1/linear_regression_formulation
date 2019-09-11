import re
import numpy as np
import matplotlib.pyplot as plt

non_decimal = re.compile(r'[^\d]+')

X = []
Y = []

for line in open('moore.csv'):
    r =  line.split('\t')
  
    x = int(non_decimal.sub('', r[2].split('[')[0]))
    y = int(non_decimal.sub('', r[1].split('[')[0]))
    X.append(x)
    Y.append(y)

X = np.array(X)
Y = np.array(Y)

plt.scatter(X,Y)
plt.show()

Y = np.log(Y)

denominator = X.dot(X) - X.mean() * X.sum()
a = ( X.dot(Y) - Y.mean()*X.sum() ) / denominator
b = ( Y.mean() * X.dot(X) - X.mean() * X.dot(Y) ) / denominator

yhat = a*X + b

plt.scatter(X,Y)
plt.plot(X,yhat)
plt.show()
rss = Y - yhat
tss = Y - Y.mean()

r2 = 1 - (rss.dot(rss)/tss.dot(tss))