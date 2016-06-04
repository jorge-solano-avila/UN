import sys

n = int( sys.stdin.readline() )

array = []

for i in xrange( n ):
	array.append( int( sys.stdin.readline() ) )

array.sort()

for x in array:
	print x