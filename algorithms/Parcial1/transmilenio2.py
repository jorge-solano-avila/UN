import sys

def centrality( G, v, aux ):
	distance = {}
	oList = [v]
	distance[v] = 0
	result = 0
	while len( oList ) > 0:
		current = oList.pop( 0 )
		for neighbor in G[current]:
			if neighbor not in distance:
				distance[neighbor] = distance[current] + 1
				if neighbor in aux:
					result += distance[neighbor]
				oList.append( neighbor )
	return result

def make_link( G, node1, node2 ):
	if node1 not in G:
		G[node1] = {}
	( G[node1] )[node2] = 1
	return G

t = int( sys.stdin.readline() )
k = 1
while t > 0:
	n, m = map( int, sys.stdin.readline().split() )
	aux = m
	array = []
	G = {}
	routes = [0 for x in xrange( n )]
	while aux > 0:
		array = map( int, sys.stdin.readline().split() )
		for i in xrange( 1, len( array ) ):
			routes[array[i] - 1] += 1
			if i != len( array ) - 1:
				make_link( G, array[i], array[i + 1] )
		aux -= 1
	aux = []
	#print routes
	for i in xrange( len( routes ) ):
		if routes[i] >= 2:
			aux.append( i + 1 )
	aux.sort()
	minim = 'INF'
	station = 0
	#print aux
	for i in xrange( len( aux ) ):
		c = centrality( G, aux[i], aux )
		if c < minim:
			station = aux[i]
			minim = c
	print "Caso %d:" % ( k )
	print station, minim
	k += 1
	t -= 1
	