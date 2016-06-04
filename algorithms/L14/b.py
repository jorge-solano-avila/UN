import sys

def makeLink( G, u, v, t ):
	if u not in G:
		G[u] = {}
	G[u][v] = t
	if v not in G:
		G[v] = {}
	G[v][u] = t

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
	G = {}
	n, m, q = map( int, sys.stdin.readline().split() )
	while m > 0:
		edge1, edge2, k = map( int, sys.stdin.readline().split() )
		makeLink( G, edge1, edge2, k )
		m -= 1
	while q > 0:
		initial, final = map( int, sys.stdin.readline().split() )
		if initial == final:
			print 0
		elif initial not in G:
			print -1
		else:
			s = dijkstra( G, initial, final ) 
			if final not in s:
				print -1
			else: 
				print s[final]
		q -= 1