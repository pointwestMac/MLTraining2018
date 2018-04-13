import numpy as np
import time

# load dataset
dataset = np.loadtxt("ex4-data.csv", delimiter=",",skiprows=1)

# Create a function that takes in two numpy array X, initializes
# parameter matrices w1, b1, w2, b2
def abc(X, n_h):
    w1 = np.zeros((X.shape[1],n_h))
    b1 = np.zeros((n_h,1))
    w2 = np.zeros(w1.shape)
    b2 = np.zeros((1,1))
    return w1, b1, w2, b2

w1, b1, w2, b2 = abc(dataset, 2)

print(w1.shape)
print(b1.shape)
print(w2.shape)
print(b2.shape)
