import sys

def ifPow( item ):
	aux = item
	if aux[0] == "1":
		for i in xrange( 1, len( aux ) ):
			if aux[i] != "0":
				return False
	else:
		return False
	return True

t = int( sys.stdin.readline() )

for i in xrange( t ):
	n = int( sys.stdin.readline() )
	array = map( str, sys.stdin.readline().split() )
	b = "1"
	for item in array:
		if ifPow( item ):
			b += "0" * ( len( item ) - 1 )
		elif item == "0":
			b = "0"
			break
		else:
			b = item + b[1:]
	print b