import sys

def makeLink( G, u, v ):
	if u not in G:
		G[u] = {}
	G[u][v] = 1
	if v not in G:
		G[v] = {}
	G[v][u] = 1

t = int( sys.stdin.readline() )

while t > 0:
	n, m = map( int, sys.stdin.readline().split() )
	no = False
	G = {}
	for i in xrange( m ):
		u, v = map( int, sys.stdin.readline().split() )
		makeLink( G, u, v )
	array = map( int, sys.stdin.readline().split() )
	for vertex1 in array:
		for vertex2 in array:
			if vertex1 == vertex2:
				continue
			if vertex2 not in G[vertex1]:
				print "NO"
				no = True
				break
		if( no ):
			break
	if( not no ):
		print "SI"
	t -= 1