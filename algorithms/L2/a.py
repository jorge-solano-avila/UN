import sys

n = int( sys.stdin.readline() )

for i in xrange( n ):
	a = int( sys.stdin.readline() )
	count = 0
	for j in xrange( a ):
		array = sys.stdin.readline()
		for k in xrange( len( array ) ):
			if array[k] == "#":
				count += 1
	print count