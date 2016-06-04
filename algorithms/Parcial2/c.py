import sys

def media( matrix ):
	array = matrix[:]
	n = 0
	result = 0
	for i in xrange( len( array ) ):
		for j in xrange( len( array[i] ) ):
			if not array[i][j] == float( 'Inf' ):
				result += array[i][j]
				n += 1
	return ( result * 1.0 ) / ( n * 1.0 )

def median( matrix ):
	array = matrix[:]
	result = []
	for i in xrange( len( array ) ):
		for j in xrange( len( array[i] ) ):
			if not array[i][j] == float( 'Inf' ):
				result.append( array[i][j] )
	n = len( result )
	result.sort()
	if n % 2 == 0:
		return int( ( result[n / 2] + result[n / 2 - 1] ) / 2 )
	return result[n / 2]

def floydWarshall( w ):
	n = len( w )
	d = w[:]
	for i in xrange( n ):
		for j in xrange( n ):
			for k in xrange( n ):
				d[j][k] = min( d[j][k], d[j][i] + d[i][k] )
	return d

t = int( sys.stdin.readline() )

while t > 0:
	n, m = map( int, sys.stdin.readline().split() )
	weigths = []
	for i in xrange( n ):
		weigths.append( [float( 'Inf' ) for j in xrange( n )] )

	for i in xrange( n ):
		for j in xrange( n ):
			if i == j:
				weigths[i][j] = 0
	for i in xrange( m ):
		u, v, w = map( int, sys.stdin.readline().split() )
		weigths[u - 1][v - 1] = w
	array = floydWarshall( weigths )
	print round( media( array ), 2 ), median( array )
	t -= 1