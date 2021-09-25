a = int(input('Write the length of first side of a triangle: '))
b = int(input('Write the length of second side of a triangle: '))
c = int(input('Write the length of third side of a triangle: '))
p = (a+b+c)/2
from math import sqrt
s = sqrt(p*(p-a)*(p-b)*(p-c))
print('The area of a triangle is ', s)