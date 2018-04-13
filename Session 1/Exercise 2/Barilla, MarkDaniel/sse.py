import numpy as np

# load dataset
dataset = np.loadtxt("ex2-data.csv", delimiter=",", skiprows=1)
X = dataset[:, 0]
Y = dataset[:, 1]

# Takes two numpy arrays, x and y, and computes the SSE.
def sse(x, y):
    return sum((x-y)**2)/(2*(X.size))

# Print out the SSE of X and Y.
print(sse(X, Y))
