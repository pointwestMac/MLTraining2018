import numpy as np
import time

# load dataset
dataset = np.loadtxt("ex2-data.csv", delimiter=",",skiprows=1)
X = dataset[:,0]
Y = dataset[:,1]

print(len(X))
print(len(Y))


# using for loop
start = time.time()
Z = 0
for i in list(range(0,len(X))):
    Z += X[i]*Y[i]
print(Z)
stop = time.time()
print("Method 1: %s" % str(stop - start))


# using matrix multiplication and sum
start = time.time()
Z = sum(X*Y)
print(Z)
stop = time.time()
print("Method 2: %s" % str(stop - start))


# Create a function that takes in two numpy arrays, f(x), y that returns SSE
def return_sse(Yhat, Y):
    n = len(Yhat)
    SSE = sum((Yhat-Y)**2)/(2*n)
    return SSE
