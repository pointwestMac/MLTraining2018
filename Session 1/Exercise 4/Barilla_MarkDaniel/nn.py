import numpy as np

# Load dataset.
dataset = np.loadtxt("ex4-data.csv", delimiter=",", skiprows=1)
age = dataset[:, 0]
height = dataset[:, 1]
weight = dataset[:, 2]

# Create a function that initializes parameter matrices and returns them.
def init_params(X, n_h):
    """Creates the parameter matrices for a 2-layer neural network with `n_h` units in the hidden layer
    and one output neuron.
    
    Arguments:
        X {np.array} -- The matrix containing all the input data.
        n_h {integer} -- Number of neurons in the hidden layer.
    """
    W_1 = np.random.rand(X.shape[1], n_h)   # Weight matrix for connecting the input layer 
                                            # to the first hidden layer with n_h neurons
                                            # Input layer will have as many neurons as columns in dataset.

    b_1 = np.random.rand(n_h)               # Offset values of the n_h neurons in the first hidden layer.

    W_2 = np.random.rand(n_h, 1)            # Weight matrix for the connecting the first hidden layer
                                            # to the output layer with 1 neuron.

    b_2 = np.random.rand(1)                 # Offset value of the output neuron.
    
    return W_1, b_1, W_2, b_2

# Print out the shapes of the initialized parameter matrices.
W_1, b_1, W_2, b_2 = init_params(dataset, 10)
print(W_1.shape)
print(b_1.shape)
print(W_2.shape)
print(b_2.shape)