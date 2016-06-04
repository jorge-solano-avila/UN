import sys
import heapq
import time

def calculateDistance( my, you ):
	return ( my[0] - you[0] ) ** 2 + ( my[1] - you[1] ) ** 2

def minPoint( distances, key ):
	aux = distances[key]
	flag = False
	result = []
	for item in aux:
		if not flag:
			result = item
			flag = True
			continue
		if item[0] < result[0]:
			result = item
		elif item[0] == result[0] and item[1] < result[1]:
			result = item
	return tuple( result )

n = int( sys.stdin.readline().strip() )

for i in xrange( n ):
	print "Caso #" + str( i + 1 ) + ":"
	array = []
	distances = {}
	distancesTotals = {}
	my = map( int, sys.stdin.readline().strip().split() )
	positions = {}
	q = int( sys.stdin.readline().strip() )
	for j in xrange( q ):
		you = map( int, sys.stdin.readline().strip().split() )
		if( you[0] == 1 ):
			if tuple( you[1:] ) not in positions:
				distance = calculateDistance( my, you[1:] )
				if distance not in distances:
					distances[distance] = tuple( you[1:] )
					distancesTotals[distance] = {}
					distancesTotals[distance][tuple( you[1:] )] = 1
					temp = []
					temp.append( distance )
					temp.append( tuple( you[1:] ) )
					heapq.heappush( array, tuple( temp ) )
					positions[tuple( you[1:] )] = 1
				else:
					distancesTotals[distance][tuple( you[1:] )] = 1
					distances[distance] = minPoint( distancesTotals, distance )
					temp = []
					temp.append( distance )
					temp.append( tuple( you[1:] ) )
					heapq.heappush( array, tuple( temp ) )
					positions[tuple( you[1:] )] = 1
		else:
			aux = {}
			for k in xrange( you[1] ):
				if k == you[1] - 1:
					if len( array ) > 0:
						element = heapq.heappop( array )
						heapq.heappush( array, element )
						print " ".join( map( str, distances[element[0]] ) )
					else:
						print -1
				else:
					if len( array ) > 0:
						element = heapq.heappop( array )
						aux[element] = 1
						dictionary = distancesTotals[element[0]]
						del dictionary[element[1]]
						distancesTotals[element[0]] = dictionary
						distances[element[0]] = minPoint( distancesTotals, element[0] )
					else:
						print -1
						break
			for item in aux:
				heapq.heappush( array, item )
				distancesTotals[item[0]][item[1]] = 1
				distances[item[0]] = minPoint( distancesTotals, item[0] )