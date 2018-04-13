import numpy as np

# Load dataset.
dataset = np.loadtxt("ex3-data.csv", delimiter=",", skiprows=1)
Y = dataset[:, 0]
X = dataset[:, 1]

# Takes two numpy arrays and computes the Logistic Regression Error Function.
def lref(x, y):
    return sum(y*np.log(x) + (1-y)*np.log(1-x))/(-x.size)

# Print out the LREF of X and Y.
print(lref(X, Y))
