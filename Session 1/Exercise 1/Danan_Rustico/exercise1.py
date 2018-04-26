import numpy as np
import time


# load dataset
dataset = np.loadtxt("test-data.csv", delimiter=",",skiprows=1)
X = dataset[:,0]
Y = dataset[:,1]

#test print
print("No Errors!")

start_time = time.time()
Z=[]
for rusticopogi in range(len(X)):
    product = X[rusticopogi] * Y[rusticopogi]
    Z.append(product)

print(sum(Z))
timex = time.time() - start_time
print("--- %s seconds ---" % (timex))



start_time = time.time()
Z= np.matmul(X,Y)
print(Z)
timey = time.time() - start_time
print("--- %s seconds ---" % (timey))


timez = timex-timey

print ("Numpy Matmul is faster than for loops by %s seconds" % (timez))
