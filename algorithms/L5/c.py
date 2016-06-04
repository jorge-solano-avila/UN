import sys

n = int( sys.stdin.readline() )

while n > 0:
	a = map( int, sys.stdin.readline().split() )
	b = sum( a ) / 2
	if b == len( a ) - 1:
		print "Arbol"
	else:
		print "No arbol"
	n -= 1