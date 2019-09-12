import numpy as np
import matplotlib.pyplot as plt
#row and column defnition
N = 10
D = 3

X = np.zeros([N,D])

X[:,0] = 1
X[:5,1] = 1
X[5:,2] = 1
Y = np.array([0]*5 + [1]*5)

#random initialization
w = np.random.rand(D)/np.sqrt(D)
learning_rate = 0.001 #assingning the learning rate
costs=[] #storing the mse
for t in range(1000):
    Yhat =  X.dot(w)
    delta = Yhat - Y 
    w = w - learning_rate*X.T.dot(delta)

    mse = delta.dot(delta)/N
    costs.append(mse)


plt.plot(costs)
plt.show()
print("final weights value",w)
plt.plot(Y,label='actual')
plt.plot(Yhat,label='predicted')
plt.title('predicted vs actual')
plt.legend()



