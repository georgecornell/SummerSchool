import sys


if len(sys.argv)<3:
	print "Not enough parameters"
	sys.exit(0)
	
try:
	a = int(sys.argv[1])
except:
	print "Invalid input provided for first argument"
	sys.exit(0)

if a<0:
	print "Input must be positive"
	sys.exit(0)	
try:
	b = sys.argv[2]
	file = open(b, "w")
except:
	print "File name error"
	sys.exit(0)



file.write(str(a))

n = 0

while (a>1):
    n=n+1
    if a%2==0:
        ## a is then divided by two if even
        a=a/2
        
    else:
        ## a is multiplied by 3 and 1 is added if odd
        a=3*a + 1

    file.write(" ")
    file.write(str(a))

file.write("\n")
file.close()

print n
