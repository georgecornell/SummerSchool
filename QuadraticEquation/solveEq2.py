import sys
import math, cmath

try:
  a = float(sys.argv[1])
  b = float(sys.argv[2])
  c = float(sys.argv[3])
  
  if a==b==c==0:
    print "Infinite number of solutions"
  else:  
    d = b*b-4*a*c
    x = -b/2*a
    y = cmath.sqrt(d)/(2*a) if d < 0 else math.sqrt(d)/(2*a)

    print str(x + y)
    if (y):
      print str(x - y)
  
except IndexError:
  print 'Not enough arguments'
except ValueError:
  print 'Program arguments must be numbers' 
except ZeroDivisionError:
  print 'first argument(a) may not be zero'

