import sys

t = int( sys.stdin.readline() )

while t > 0:
	alphabet = map( str, sys.stdin.readline().split() )
	aux = {}
	for item in alphabet:
		aux[item] = 0
	string = sys.stdin.readline().strip()
	for item in string:
		aux[item] += 1
	result = []
	for item in alphabet:
		temp = aux[item]
		if temp > 0:
			for j in xrange( temp ):
				result.append( item )
	print "".join( result )
	t -= 1

"""
while t > 0:
	alphabet = map( str, sys.stdin.readline().split() )
	aux = [0] * len( alphabet )
	string = sys.stdin.readline().strip()
	for i in xrange( len( string ) ):
		for j in xrange( len( alphabet ) ):
			if string[i] == alphabet[j]:
				aux[j] += 1
				break
	result = []
	for i in xrange( len( alphabet ) ):
		if aux[i] > 0:
			for j in xrange( aux[i] ):
				result.append( alphabet[i] )
	print "".join( result )
	t -= 1
"""