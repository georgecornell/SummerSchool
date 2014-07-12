import sys

def addto(var, val):
    var.append( val )

def wf(n, v):
    n.write(v)

def func():
    output = 0
    dest = "C:\\Python27\\"
    try:
        number = int(sys.argv[1])
        saveto = str(sys.argv[2])
        checksaveto = saveto.split("\\")
        nums = [number]

        if number < 1:
            print "You must enter an integer that is greater than zero. Please try again."
        
        elif len(checksaveto) < 3:
            print "Please enter the file's entire directory."
            
        else:
            while number != 1:
                if number % 2 == 0:
                    number = number/2
                else:
                    number = (number*3) + 1
                output = output + 1
                addto(nums, number)
            else:
                print output
                print "File written and saved in the specified location."
                with open(saveto, 'w') as f:
                    for i in nums:
                        wf(f, str(i) + "\n")

    except IndexError:
        print "You did not enter enough arguments. Usage:"
        print "...computeCollatz.py [integer to be passed through sequence] [directory and name of file to be created and saved]"
func()
