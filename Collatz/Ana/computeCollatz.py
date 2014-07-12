import sys

# Read command argv.

try:
	n = int(sys.argv[1])
	filename = sys.argv[2]

	if n < 1 :
		print 'Need positive integer'
		sys.exit()

	# Open the file

	x = open(filename, "w")


	# Compute Collatz Sequence
	seqlen = 0
	while n > 1:

		## For even numbers (n/2)
	 	if n%2 == 0:
	 		n = n/2
		## For odd numbers (3n+1)
		else:
			n = 3*n + 1
		seqlen = seqlen + 1



		## Write to the file
		x.write(str(n)+"\n")

	## Increment sequence length

	print seqlen
	## Repeat until Number in sequence is 1

	# Close file
	x.close()

except ValueError:
	print 'Need positive integer'
except IOError:
	print 'Invalid file name'
except IndexError:
	print 'Need two argv'

	# Print length

