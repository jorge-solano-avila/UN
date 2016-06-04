import sys

def make_link( G, node1, node2 ):
    if node1 not in G:
        G[node1] = {}
    ( G[node1] )[node2] = 1
    if node2 not in G:
        G[node2] = {}
    ( G[node2] )[node1] = 1
    return G

def BFS_iterative( G, node ):
    color = {}
    parent = {}
    for v in G:
        color[v] = 'white'
        depth[v] = float( 'Inf' )
    color[node] = 'gray'
    parent[node] = None
    nodelist = [node]
    total_marked = 1
    while nodelist <> []:
        u = nodelist.pop(0)
        for neighbor in G[u]:
            if color[neighbor] == 'white':
                color[neighbor] = 'gray'
                parent[neighbor] = u
                nodelist.append( neighbor )
                total_marked += 1
        color[u] = 'black'
    return total_marked, parent

t = int( sys.stdin.readline() )

while t > 0:
	n, m = map( int, sys.stdin.readline().split() )
	G = {}
	"""
	while m > 0:
		a, b = map( int, sys.stdin.readline().split() )
		make_link( G, a, b )
		array[a] += 1
		array[b] += 1
		m -= 1
	friends = array[0]
	maxim = 0
	for i in xrange( 1, n ):
		if array[i] > friends:
			friends = array[i]
			maxim = i
	print maxim, friends"""
	while m > 0:
		a, b = map( int, sys.stdin.readline().split() )
		make_link( G, a, b )
		m -= 1
	maxim, friends = 0, 0
	for v in G:
		lenV = len( G[v] )
		if lenV > friends:
			friends = lenV
			maxim = v
	print maxim, friends
	t -= 1