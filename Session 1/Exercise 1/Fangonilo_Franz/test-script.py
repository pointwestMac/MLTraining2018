import numpy as np
import time

# load dataset
dataset = np.loadtxt("test-data.csv", delimiter=",",skiprows=1)
X = dataset[:,0]
Y = dataset[:,1]

#test print
print("No Errors!")

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
