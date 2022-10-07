from math import *

a = float(input())
b = float(input())
c = float(input())

D = b ** 2 - 4 * a * c
if D < 0:
    print('Нет корней')
elif D == 0:
    print(-b / (2 * a))
else:
    x1 = (-b - sqrt(D)) / (2 * a)
    x2 = (-b + sqrt(D)) / (2 * a)
    if x1 < x2:
        print(x1)
        print(x2)
    else:
        print(x2)
        print(x1)
