import numpy as np
import time

# load dataset
dataset = np.loadtxt("test-data.csv", delimiter=",",skiprows=1)
X = dataset[:,0]
Y = dataset[:,1]

#test print
#print("No Errors!")

#print length arrays in console
print("Length of x: {0}".format(len(X)))
print("Length of y: {0}".format(len(Y)))

#compute Z

#for loop

start1 = time.time()

item = 0
for ith in range(0, len(Y)):
    item += X[ith]*Y[ith]

end1 = time.time()

print("Total time for loop: ", end1 - start1)

#matrix multiplication and sum

start2 = time.time()

mult = np.multiply(X, Y)
summed = sum(mult)

end2 = time.time()

print("Total time for multiply + sum: ", end2 - start2)
