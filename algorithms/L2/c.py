import sys

n = int( sys.stdin.readline() )

def add( array ):
	count = 0
	for item in array:
		count += item
	return count

def ifCut( array ):
	for i in xrange( len( array ) ):
		for j in xrange( i + 1, len( array ) ):
			if add( array[:i + 1] ) == add( array[i + 1:] ):
				return True
			if add( array[:i + 1] ) < add( array[i + 1:] ):
				break 
	return False

for i in xrange( n ):
	a = int( sys.stdin.readline() )
	tempRow = [] 
	tempCol = []
	matrix = []
	for j in xrange( a ):
		matrix.append( raw_input() )

	for j in xrange( a ):
		count = 0
		for k in xrange( a ):
			if matrix[j][k] == "#":
				count += 1
		tempRow.append( count )
	for j in xrange( a ):
		count = 0
		for k in xrange( a ):
			if matrix[k][j] == "#":
				count += 1
		tempCol.append( count )
	if ifCut( tempRow ) or ifCut( tempCol ):
		print "YES"
	else:
		print "NO"