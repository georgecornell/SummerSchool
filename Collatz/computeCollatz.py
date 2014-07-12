import sys

def collatz(n, filehandle):
    seqLength = 0
    while n != 1:
      #n = n/2 if (n%2 == 0) else 3*n+1
      n = (n << 1) + n + 1 if n & 1 else n >> 1
      filehandle.write(str(n)+"\n")
      seqLength += 1
    filehandle.close()
    return seqLength

def validateArguments(args, validArguments):
  try:
    n = int(args[1])
    if n < 2:
      print 'Collatz sequence may not be less than 2'
    filename = args[2]
    filehandle = open(filename, "w")

    validArguments.append(n)
    validArguments.append(filehandle)
    return True
  
  except IndexError:
    print 'Not enough arguments'
  except ValueError:
    print 'First program argument must be a pozitive integer'
  except IOError:
    print 'Cannot open file %s' % sys.argv[2]
  return False

if __name__ == '__main__':
  validArguments = []
  if validateArguments(sys.argv,validArguments):
    n, filehandle = validArguments
    collatzLength = collatz(n, filehandle)
    print collatzLength
