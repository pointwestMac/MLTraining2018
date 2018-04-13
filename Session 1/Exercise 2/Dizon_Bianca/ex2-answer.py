import numpy as np

#import dataset
dataset = np.loadtxt(open("ex2-data.csv", "rb"), delimiter=",", skiprows=1)

#compute SSE
num = sum((dataset[:,0] - dataset[:,1])**2)
den =  2*len(dataset[:,1])
final = num / den

print("The SSE is {0}.".format(final))
