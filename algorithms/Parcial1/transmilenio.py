import sys

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
	result = {}
	routes = [0 for x in xrange( n )]
	while aux > 0:
		array = map( int, sys.stdin.readline().split() )
		for i in xrange( 1, len( array ) ):
			routes[array[i] - 1] += 1
		aux -= 1
	aux = []
	for i in xrange( len( routes ) ):
		if routes[i] >= 2:
			aux.append( i + 1 )
	aux.sort()
	stringa = ""
	print "Caso %d:" % ( k )		
	print " ".join( map( str, aux ) )
	stations = []
	for i in xrange( len( aux ) ):
		stations.append( routes[aux[i] - 1] )
	print " ".join( map( str, stations ) )
	k += 1
	t -= 1