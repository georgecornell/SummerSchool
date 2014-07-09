

import sys

print sys.argv

a = sys.argv[2]
b = sys.argv[1]
c = sys.argv[3]

print a

x1 = (-b + (b * b - 4 * a * c) ** 0.5)/(2 * a)
x2 = (-b - (b * b - 4 * a * c) ** 0.5)/(2 * a)

print x1, x2