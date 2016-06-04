import sys

globa = {}

def makeLink( G, u, v, t ):
	if u not in G:
		G[u] = {}
	G[u][v] = t

def shortest( dist ):
	bNode = 'undefined'
	bValue = 100000
	for v in dist:
		if dist[v] < bValue:
			( bNode, bValue ) = ( v, dist[v] )
	return bNode

def dijkstra( G, v, final ):
	s = {}
	s[v] = 0
	q = {}
	while final not in q:
		w = shortest( s )
		if w == 'undefined':
			return q
		q[w] = s[w]
		del s[w]
		if w in G:
			for x in G[w]:
				if x not in q:
					if x not in s:
						s[x] = q[w] + G[w][x]
					elif q[w] + G[w][x] < s[x]:
						s[x] = q[w] + G[w][x]
	return q

t = int( sys.stdin.readline() )

for i in xrange( t ):
	print "Case #" + str( i + 1 ) + ":"
	G = {}
	globa = {}
	cells, initial, final = map( int, sys.stdin.readline().split() )
	edges = int( sys.stdin.readline() )
	while edges > 0:
		edge1, edge2, time = map( int, sys.stdin.readline().split() )
		if not edge1 == edge2:
			makeLink( G, edge1, edge2, time )
		edges -= 1
	if initial not in G:
		print -1
		continue
	s = dijkstra( G, initial, final )
	if final not in s:
		print -1
		continue
	print s[final]