import sys

t = int( sys.stdin.readline() )

while t > 0:
	n = int( sys.stdin.readline() )
	array = map( int, sys.stdin.readline().split() )
	result = [0] * 100
	for item in array:
		result[item] += 1
	for i in xrange( 99, -1, -1 ):
		if result[i] > 0:
			print i,
	print
	t -= 1