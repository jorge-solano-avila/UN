import sys

n = int( sys.stdin.readline() )

while n > 0:
	a = int( sys.stdin.readline() )
	print a ** 3 + 3 * ( a ** 2 ) + 4 * a + 3
	n -= 1