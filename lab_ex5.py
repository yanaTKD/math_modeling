a = int(input())
b = int(input())
if b == 0:
    print('NUUUUUUUL!!!!!')
elif a % b == 0:
    print('NA ZELO', a // b)
else:
    print('NE NA ZELO', a // b, a % b)