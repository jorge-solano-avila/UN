import sys

def mul2( matrix1, matrix2 ):
	matrix = []
	array = []
	for i in xrange( len( matrix1 ) ):
		array.append( matrix1[i][0] * matrix2[0][0] + matrix1[i][1] * matrix2[1][0] )
		array.append( matrix1[i][0] * matrix2[0][1] + matrix1[i][1] * matrix2[1][1] )
		matrix.append( array )
		array = []
	return matrix

def mul( matrix, n ):
	if n == 0:
		return 1
	elif n == 1:
		return matrix
	elif n % 2 == 0:
		return mul2( mul( matrix, n / 2 ), mul( matrix, n / 2 ) )
	return mul2( matrix, mul2( mul( matrix, n / 2 ), mul( matrix, n / 2 ) ) )

t = int( sys.stdin.readline() )

while( t > 0 ):
	n = int( sys.stdin.readline() )
	matrix = []
	for i in xrange( 2 ):
		matrix.append( map( int, sys.stdin.readline().split() ) )
	#print matrix
	matrix1 = []
	array = []
	matrix = mul( matrix, n )
	for i in xrange( len( matrix ) ):
		for j in xrange( len( matrix[i] ) ):
			if j == len( matrix[i] ) - 1:
				print str( matrix[i][j] ).replace( "L", " " )
			else:
				print str( matrix[i][j] ).replace( "L", " " ),
	print
	t -= 1