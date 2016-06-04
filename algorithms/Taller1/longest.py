import sys

def make_link( G, node1, node2 ):
    if node1 not in G:
        G[node1] = {}
    ( G[node1] )[node2] = 1
    if node2 not in G:
        G[node2] = {}
    ( G[node2] )[node1] = 1
    return G

"""
def DFS_Visit_p( G, node, color, parent ):
    color[node] = 'gray'
    total_marked = 1
    for neighbor in G[node]:
        if color[neighbor] == 'white':
            parent[neighbor] = node
            total_marked += DFS_Visit_p( G, neighbor, color, parent )
    color[node] = 'black'
    return total_marked

def make_link( G, node1, node2 ):
    if node1 not in G:
        G[node1] = {}
    ( G[node1] )[node2] = 1
    if node2 not in G:
        G[node2] = {}
    ( G[node2] )[node1] = 1
    return G

def path( G, v1, v2 ):
    color = {}
    parent = {}
    for v in G:
        color[v] = 'white'
        parent[v] = None
    DFS_Visit_p( G, v1, color, parent )
    #display_parent( parent )
    node = v2
    pathlist = [node]
    while node <> None:
        node = parent[node]
        #print 'node = ', node
        if node <> None:
            pathlist = [node] + pathlist
    if color[v2] == 'black':
        return pathlist # los vertices en pathlist estan en orden inverso, [::-1] los invierte
    else:
        return []
"""
n = int( sys.stdin.readline() )
G = {}

while n - 1 > 0:
	u, v = map( int, sys.stdin.readline().split() )
	make_link( G, u, v )
	n -= 1 

dist = {}

for v in G.keys():
	dist[v] = v
	dist[v][v] = 0

for u, values in G.iteritems():
	for v in values:
		dist[u][v[0]] = v[1] 

for k in G.keys(): 
    for i in G.keys(): 
        for j in G.keys(): 
            if dist[i][j] > dist[i][k] + dist[k][j]: 
                dist[i][j] = dist[i][k] + dist[k][j]

print max( product( dist.keys(), dist.keys() ), key = lambda x: dist[x[0]][x[1]] )

"""
longest = 0
keys = G.keys()
for i in xrange( len( keys ) ):
	for j in xrange( i + 1, len( keys ) ):
		if keys[i] == keys[j]:
			continue
		aux = len( path( G, keys[i], keys[j] ) )
		if aux > longest:
			longest = aux

print longest - 1
"""