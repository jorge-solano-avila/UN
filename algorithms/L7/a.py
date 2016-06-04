import sys

def posStr( i, j ):
	return str( i ) + "n" + str( j ) + "m"

def DFS_Visit( G, node, color ):
    color[node] = 'gray'
    total_marked = 1
    for neighbor in G[node]:
        if color[neighbor] == 'white':
            total_marked += DFS_Visit( G, neighbor, color )
    color[node] = 'black'
    return total_marked

def connected_components( G ):
    color = {}
    for v in G:
        color[v] = 'white'
    count = 0
    for v in G:
        if color[v] == 'white':
            count += 1
            DFS_Visit( G, v, color )
    return count

def make_link( G, node1, node2 ):
    if node1 not in G:
        G[node1] = {}
    ( G[node1] )[node2] = 1
    if node2 not in G:
        G[node2] = {}
    ( G[node2] )[node1] = 1
    return G

def result( matrix ):
	G = {}
	for i in xrange( len( matrix ) ):
		for j in xrange( len( matrix[i] ) ):
			if i != 0 and i != n - 1:
				if matrix[i - 1][j] == '@' and matrix[i][j] == '@':
					make_link( G, posStr( i - 1, j ), posStr( i, j ) )
				if j > 0 and matrix[i - 1][j - 1] == '@' and matrix[i][j] == '@':
					make_link( G, posStr( i - 1, j - 1 ), posStr( i, j ) )
				if j < len( matrix[i] ) - 1 and matrix[i - 1][j + 1] == '@' and matrix[i][j] == '@':
					make_link( G, posStr( i - 1, j + 1 ), posStr( i, j ) )
				if j > 0 and matrix[i + 1][j - 1] == '@' and matrix[i][j] == '@':
					make_link( G, posStr( i + 1, j - 1 ), posStr( i, j ) )
				if j < len( matrix[i] ) - 1 and matrix[i + 1][j + 1] == '@' and matrix[i][j] == '@':
					make_link( G, posStr( i + 1, j + 1 ), posStr( i, j ) )
				if matrix[i + 1][j] == '@' and matrix[i][j] == '@':
					make_link( G, posStr( i + 1, j ), posStr( i, j ) )
			if matrix[i][j] == '@' and j < len( matrix[i] ) - 1 and matrix[i][j + 1] == '@':
				make_link( G, posStr( i, j ), posStr( i, j + 1 ) )
			elif matrix[i][j] == '@':
				make_link( G, posStr( i, j ), posStr( i, j ) )
	return connected_components( G )

t = int( sys.stdin.readline() )

while t > 0:
	n, m = map( int, sys.stdin.readline().split() )
	temp = n
	matrix = []
	
	while temp > 0:
		row = sys.stdin.readline().strip()
		matrix.append( row )
		temp -= 1
	
	print result( matrix )
	t -= 1