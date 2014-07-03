import cmath
import sys

a = float(sys.argv[1])
b = float(sys.argv[2])
c = float(sys.argv[3])

if a < 0:
    a = -1*a
    b = -1*b
    c = -1*c

def sqrt(num):
    if num < 0:
        return cmath.sqrt(num)
    else:
        return num**0.5


answer1 = ((-1*b)-sqrt((b**2)-(4*a*c)))/(2*a)
answer2 = ((-1*b)+sqrt((b**2)-(4*a*c)))/(2*a)

if answer1 == answer2:
    print answer1
else:
    print answer1
    print answer2