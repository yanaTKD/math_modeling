import numpy as np

a = np.zeros(shape=(5))
for i in range(4):
    a[i] = int(input())
print(a)
b = int(input())
n = int(input())
a = np.insert(a,b,n)
print(a)