import numpy as np

#import dataset
dataset = np.loadtxt(open("ex4-data.csv", "rb"), delimiter=",", skiprows=1)

#create function

def initmat(X, n_h):
    """
    Function that inititalizes random paramter matrices according user
    input of number of neuron in the hidden layer.

    X is a numpy matrix of any size
    n_h is the number of neurons for the hidden layer
    """
    try:
        num_col = X.shape[1]
    except IndexError:
        num_col = 1
    
    W1 = np.random.rand(num_col, n_h)
    b1 = np.random.rand(n_h, 1)

    try:
        num_col2 = W1.shape[1]
    except IndexError:
        num_col2 = 1
        
    W2 = np.random.rand(num_col2, 1)
    b2 = np.random.rand(1, 1)
    
    return([W1, b1, W2, b2])

f = initmat(dataset,84)

print("The shape of W1 is {0}.".format(f[0].shape))
print("The shape of b1 is {0}.".format(f[1].shape))
print("The shape of W2 is {0}.".format(f[2].shape))
print("The shape of b2 is {0}.".format(f[3].shape))
