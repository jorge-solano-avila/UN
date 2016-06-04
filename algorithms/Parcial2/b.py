import sys

sys.setrecursionlimit( 100000000 )

def ways( n, array, i ):
	if n < 0:
		return 0
	elif n == 0:
		return 1

	if i == len( array ):
		return 0

	return ways( n - array[i], array, i ) + ways( n, array, i + 1 )

t = int( sys.stdin.readline() )

while t > 0:
	M = {}
	n, m = map( int, sys.stdin.readline().split() )
	array = map( int, sys.stdin.readline().split() )
	print ways( n, array, 0 )
	t -= 1