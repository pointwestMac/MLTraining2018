import numpy as np
import time

# load dataset
dataset = np.loadtxt("test-data.csv", delimiter=",",skiprows=1)
X = dataset[:,0]
Y = dataset[:,1]

#test print
print("No Errors!")

#Print out the length of the arrays X and Y.
print(X.size)
print(Y.size)

#Compute Z = sum(x_i y_i) using a loop:
start = time.process_time()
Z = 0
for i in range(0, X.size):
    Z += X[i] * Y[i]
end = time.process_time()
print(Z)
print(f"Time elapsed: {end-start}")

#Compute Z using matrix multiplication and sum.
start = time.process_time()
Z = sum(X*Y)
end = time.process_time()
print(Z)
print(f"Time elapsed: {end-start}")
