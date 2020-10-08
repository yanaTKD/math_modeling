a = int(input())
b = int(input())
c = int(input())
if a + b > c and a + c > b and b + c > a:
    print('Треугольник существует')
    if (a == b and a != c) or (a == c and a != b) or (c == b and c != a):
        print('Треугольник равнобедренный')
    elif a == b and b == c:
        print('Треугольник равносторонний')
    else:
        print('Треугольник разносторонний')
else:
    print('Треугольник не может существовать')
