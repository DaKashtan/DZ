#
#Вычисление площадей
import math
from math import tan
F = int(input('Задайте количество углов '))
def circle(r):
    S=3.14*r**2
    return S
def triangle(a,b,c):
    p = (a+b+c)/2
    S = (p*(p-a)*(p-b)*(p-c))**(1/2)
    return S
def trapezoid(a,b,c,d):
    S = ((a+b)/2)*(c**2-(((b-a)**2+c**2-d**2)/2*(b-a))**2)**(1/2)
    return S
def poligon(n,a):
    def ctg(x):
        return 1/tan(x)
    S = ((n*a**2)/4)*ctg(180/n)
    return S
if F==0:
    r = int(input('Задайте радиус '))
    s = circle(r)
elif F==3:
    a = int(input('Задайте первую сторону '))
    b = int(input('Задайте вторую сторону '))
    c = int(input('Задайте третью сторону '))
    s = triangle(a,b,c)
elif F==4:
    a = int(input('Задайте верхнее основание '))
    b = int(input('Задайте нижнее основание '))
    c = int(input('Задайте левую сторону '))
    d = int(input('Задайте правую сторону '))
    s = trapezoid(a,b,c,d)
elif F>4:
    n = F
    a = int(input('Задайте длинну стороны '))
    s = poligon(n,a)
else:
    print('Некорректные данные')
print(s)
