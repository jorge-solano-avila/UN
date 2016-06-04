import sys

def result( G, array, aux ):
	count = 0
	lenArray = len( array )
	i = lenArray - 1
	while( i >= 0 ):
		if array[i] == aux[i]:
			pass
		else:
			count += 1
			for j in xrange( ( i + 1 ) / 2 ):
				temp = array[j]
				array[j] = array[i - j]
				array[i - j] = temp
			#i += 1
		i -= 1
	if count > 1:
		return count - 1
	return count

t = int( sys.stdin.readline() )

while t > 0:
	array = map( int, sys.stdin.readline().split() )
	aux = array[:]
	aux.sort()
	G = {}
	print result( G, array, aux )
	t -= 1