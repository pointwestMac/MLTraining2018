import numpy as np
import time


# load dataset
dataset = np.loadtxt("ex2-data.csv", delimiter=",",skiprows=1)
X = dataset[:,0]
Y = dataset[:,1]

def sse(x,y):
    sse1=np.sum((x-y) ** 2)
    sse2=sse1/(2*len(x))

    print (sse2)

sse(X,Y)
