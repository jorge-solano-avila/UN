import sys

sys.setrecursionlimit( 100000000 )
coinValue = []
memo = {}

def change( n, coinValue ):
	if n < 0:
		return 10000
	if n == 0:
		return 0

	temp = []
	for i in xrange( len( coinValue ) ):
		value = n - coinValue[i]
		if value not in memo:
			aux = change( value, coinValue )
			memo[value] = aux
		else:
			aux = memo[value]
		temp.append( aux )
	minim = min( temp )
	return 1 + minim

t = int( sys.stdin.readline() )

while t > 0:
	memo = {}
	n, m = map( int, sys.stdin.readline().split() )
	coinValue = map( int, sys.stdin.readline().split() )
	result = change( n, coinValue )
	if result == 0 or result > 1000:
		print -1
	else:
		print result
	t -= 1