for i in range(2, int(input())):
    s = 0
    for j in range(1,i):
        if i%j == 0:
            s += j
    if s == i:
        print(i)