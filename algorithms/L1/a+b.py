import sys

n = int( sys.stdin.readline() )

while n > 0:
	a, b = map( int, sys.stdin.readline().split() )
	print a + b
	n -= 1