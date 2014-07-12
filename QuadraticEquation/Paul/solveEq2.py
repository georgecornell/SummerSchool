import sys
import cmath

if len(sys.argv)<4:
    print "Not enough parameters"
    sys.exit(0)


try:
    a = float(sys.argv[1])
except:
    print 'Invalid value provided for a: %s' % sys.argv[1]
    sys.exit(0)

try:
    b = float(sys.argv[2])
except:
    print 'Invalid value provided for b: %s' % sys.argv[2]
    sys.exit(0)

try:
    c = float(sys.argv[3])
except:
    print 'Invalid value provided for c: %s' % sys.argv[3]
    sys.exit(0)



det = b * b - 4 * a * c

if a==0:
    if b==0:
        if c==0:
            print 'All real solutions'
        else: 
            print 'No real solution'
    else: 
        x1=-c/b
        print 'One solution'
        print x1
else:
    if det>=0:
        #there are 2 solutions -> compute and print
        x1 = (-b + det ** 0.5)/(2 * a)
        x2 = (-b - det ** 0.5)/(2 * a)

        print x1
        print x2

    else:
        x1=(b + cmath.sqrt (det)) / (2 * a)
        x2=(-b - cmath.sqrt (det)) / (2 * a)

        print x1
        print x2



