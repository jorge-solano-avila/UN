import sys
import heapq

n = int( sys.stdin.readline() )

for i in xrange( n ):
	array = []
	arrayAux = sys.stdin.readline().split()
	result = []

	for item in arrayAux:
		if item != "*":
			heapq.heappush( array, -int( item ) )
		if item == "*":
			if len( array ) > 0:
				result.append( -heapq.heappop( array ) )
			else:
				result.append( -1 );

	print " ".join( map( str, result ) )