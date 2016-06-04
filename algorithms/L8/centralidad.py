import sys

def centrality( G, v ):
    distance = {}
    oList = [v]
    distance[v] = 0
    while len( oList ) > 0:
        current = oList.pop( 0 )
        for neighbor in G[current]:
            if neighbor not in distance:
                distance[neighbor] = distance[current] + 1
                oList.append( neighbor )
    return float( sum( distance.values() ) ) / len( distance )

def make_link( G, node1, node2 ):
    if node1 not in G:
        G[node1] = {}
    ( G[node1] )[node2] = 1
    if node2 not in G:
        G[node2] = {}
    ( G[node2] )[node1] = 1
    return G

t = int( sys.stdin.readline() )

while t > 0:
	n, m = map( int, sys.stdin.readline().split() )
	G = {}
	while m > 0:
		u, v = map( int, sys.stdin.readline().split() )
		make_link( G, u, v )
		m -= 1
	minim = 'INF'
	result = 0
	for v in G:
		value = centrality( G, v )
		if value < minim:
			minim = value
			result = v
	print result
	t -= 1