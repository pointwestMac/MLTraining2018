import numpy as np

#import dataset
dataset = np.loadtxt(open("ex3-data.csv", "rb"), delimiter=",", skiprows=1)

#create function

def logerror(sfx, y):
    """
    Function that computes for the logistic error. fx and y are numpy arrays.
    """
    summed = sum(y * np.log(sfx) + (1 - y)* np.log(1 - sfx))
    error =  - summed / len(y)
    return(error)

y = dataset[:,0]
sfx = dataset[:,1]


print("The error is {0}.".format( logerror(sfx, y) ) )
