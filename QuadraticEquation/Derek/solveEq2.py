import sys
import cmath
a = float(sys.argv[1])
b = float(sys.argv[2])
c = float(sys.argv[3])

if a < 0:
    a = a*-1
    b = b*-1
    c = c*-1

answer1 = ((-1*b) + cmath.sqrt((b**2) - (4*a*c)))/(2*a)
answer2 = ((-1*b) - cmath.sqrt((b**2) - (4*a*c)))/(2*a)

if answer1 == answer2:
	print answer1
	print "There is a double root!"
else:
	print answer1
	print answer2
	
	#discriminant = (b**2) - (4*a*c)
#answer3 = cmath.sqrt(-(b**2) - (4*a*c))j
#if discriminant < 0
#	print answer1"i"
#else:
#	print answer1
#	print answer2

