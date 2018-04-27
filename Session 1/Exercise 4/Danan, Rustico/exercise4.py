import numpy as np
import time


# load dataset
dataset = np.loadtxt("ex4-data.csv", delimiter=",",skiprows=1)

def rusticopogi(x):
    nh = int(input("Please enter number of hodes in hidden layer1: "))
    b1=np.random.rand(nh,1)
    b2=np.random.rand(1,1)
    cola= x.shape[1]

    colb1 = len(b1)
    colb2 = len(b2)
    w1=np.random.rand(cola,colb1)
    w2=np.random.rand(colb1,colb2)

    print (w1)
    print ()
    print (b1)
    print ()
    print (w2)
    print ()
    print (b2)
    
    

rusticopogi(dataset)
