import numpy as np

# load dataset
dataset = np.loadtxt("test-data.csv", delimiter=",",skiprows=1)
X = dataset[:,0]
Y = dataset[:,1]

#test print
print("No Errors!")
