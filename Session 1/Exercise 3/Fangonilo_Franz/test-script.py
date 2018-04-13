import numpy as np
import time

# load dataset
dataset = np.loadtxt("ex3-data.csv", delimiter=",",skiprows=1)
Y = dataset[:,0]
S = dataset[:,1]


# Create a function that takes in two numpy arrays, sigmoid of f(x), y that returns
# logistic regression error
def log_sse(Y, S):
    n = len(Y)
    error = (sum(Y*np.log(S)) + sum((1-Y)*np.log(1-S)))*(-1/n)
    return error

print(log_sse(Y,S))
