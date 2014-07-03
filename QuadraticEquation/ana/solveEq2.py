import sys 
import cmath,math

try:
  # Read the cmd line.
  a = float(sys.argv[1])
  b = float(sys.argv[2])
  c = float(sys.argv[3]) 

  if a == 0 and b == 0 and c == 0 :
  	print 'x equals any number'
  	sys.exit()

# Calculate Discriminant
  
  D = b*b-4*a*c

# Calculate x1,x2 when D > 0

  if D > 0 : 
	x1 = -b/(2*a) + math.sqrt(D)/(2*a)
	x2 = -b/(2*a) - math.sqrt(D)/(2*a)

# Calculate x1,x2 when D = 0

  elif D == 0 :
	x1 = x2 = -b/(2*a)

# Calculate x1,x2 when D < 0

  elif D < 0 :
	x1 = -b/(2*a) + cmath.sqrt(D)/(2*a)
	x2 = -b/(2*a) - cmath.sqrt(D)/(2*a)

# Print x1,x2

  print x1
  print x2 

except ValueError:
  print 'Need real number'
except ZeroDivisionError:
  print 'First argument may not be zero'
except IndexError:
  print 'Not enough arguments'