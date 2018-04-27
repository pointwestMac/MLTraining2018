import numpy as np
import time


# load dataset
dataset = np.loadtxt("ex3-data.csv", delimiter=",",skiprows=1)
Y = dataset[:,0]
SigmoidX = dataset[:,1]

def logerror(y,x):
    term1= y*np.log(x)
    term2= (1-y)*np.log(1-x)
    sumans = np.sum(term1+term2)
    J = (-1/len(x)) * (sumans)

    print (J)


logerror(Y, SigmoidX)
