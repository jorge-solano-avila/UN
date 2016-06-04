def isCycle( G ):
	nodes = len( G )
	vertex = 0
	for v in G:
		vertex += len( G[v] )
	vertex /= 2
	if vertex < nodes:
		return False
	return True

def make_link( G, node1, node2 ):
    if node1 not in G:
        G[node1] = {}
    ( G[node1] )[node2] = 1
    if node2 not in G:
        G[node2] = {}
    ( G[node2] )[node1] = 1
    return G

def DFS_Visit( G, node, color ):
    color[node] = 'gray'
    total_marked = 1
    for neighbor in G[node]:
        if color[neighbor] == 'white':
            total_marked += DFS_Visit( G, neighbor, color )
    color[node] = 'black'
    return total_marked

edges1 = [( 'v', 'r' ), ( 'r', 's' ), ( 'w', 't' ), ( 's','w' ),
         ( 'w', 'x' ), ( 't', 'x' ), ( 't', 'u' ), ( 'x', 'y' ),
         ( 'u', 'y' )]

G = {}
for v1, v2 in edges1:
	make_link( G, v1, v2 )

print isCycle( G )