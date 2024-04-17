import math

x1 = int(input('x1: '))
y1 = int(input('y1: '))
x2 = int(input('x2: '))
y2 = int(input('y2: '))
x3 = int(input('x3: '))
y3 = int(input('y3: '))
a = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
b = math.sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
c = math.sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2)
p = (a+b+c)/2
s = math.sqrt(p * (p - a) * (p - b) * (p - c))
print(f"Площадь = {s}")
print(f"Периметр = {p * 2}")