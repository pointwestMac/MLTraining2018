import numpy as np
import time

# load dataset
dataset = np.loadtxt("test-data.csv", delimiter=",",skiprows=1)
X = dataset[:,0]
Y = dataset[:,1]

#test print
print("No Errors!")
print(len(X))
print(len(Y))

start_time = time.time()
Z = []
for i in range(0, len(X)-1):
    Z.append(X[i]*Y[i])

print(sum(Z))
for_time = time.time() - start_time
print("For loop ran for %s seconds ---" % (for_time))

start_time = time.time()
print(np.matmul(X, Y))
mat_time = time.time() - start_time
print("Matrix multiplication ran for %s seconds ---" % (mat_time))


if mat_time > for_time:
      print("For loop is faster by")
elif for_time > mat_time:
      print("Matrix multiplication is faster by")
else:
      print("Both fast")


print("% s seconds" % (max(for_time, mat_time) - min(for_time, mat_time)))
      




