import numpy as np

a = np.zeros(shape=(2, 3))
b = np.zeros(shape=(2, 3))
c = np.zeros(shape=(2, 3))

for (i, j), x in np.ndenumerate(a):
    a[i, j] = int(input())
print(a)
for (i, j), y in np.ndenumerate(b):
    b[i, j] = int(input())
print(b)
for (i, j), x in np.ndenumerate(a):
    if a[i,j] > b[i,j]:
        c[i,j] = x
    elif a[i,j] == b[i,j]:
        c[i,j] = x
    else:
        c[i,j] = y
print(c)