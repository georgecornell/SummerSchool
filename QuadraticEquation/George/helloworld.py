import sys
########
print ("Quadratic Equation Calculator v2.3")
########
a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])
########
x = ( -(b) + ( ( ((b) ** 2) - ( 4 * (a) * (c) ) ) ** 0.5 ) )/ ((a) * 2 ) 
y = ( -(b) - ( ( ((b) ** 2) - ( 4 * (a) * (c) ) ) ** 0.5 ) )/ ((a) * 2 ) 
########
print (x)
print (y)
