import sys

n = int( sys.stdin.readline() )

for i in xrange( n ):
	a = int( sys.stdin.readline() )
	col = a
	row = a
	tempRow = 0 
	tempCol = 0
	matrix = []
	for j in xrange( a ):
		matrix.append( raw_input() )

	for j in xrange( a ):
		count = 0
		for k in xrange( a ):
			if matrix[j][k] == "#":
				count += 1
		if count > tempRow:
			tempRow = count
			row = j + 1
	for j in xrange( a ):
		count = 0
		for k in xrange( a ):
			if matrix[k][j] == "#":
				count += 1
		if count > tempCol:
			tempCol = count
			col = j + 1
	print row, col