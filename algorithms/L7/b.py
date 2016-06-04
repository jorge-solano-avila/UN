import sys
"""
aux = []

def make_link( G, aux1, aux2 ):
    if aux1 not in G:
        G[aux1] = {}
    ( G[aux1] )[aux2] = 1
    if aux2 not in G:
        G[aux2] = {}
    ( G[aux2] )[aux1] = 1
    return G

def BFS_iterative( G, aux ):
    color = {}
    depth = {}
    parent = {}
    for v in G:
    	color[v] = 'white'
    	depth[v] = float( 'Inf' )
    color[aux] = 'gray'
    depth[aux] = 0
    parent[aux] = None
    auxlist = [aux]
    total_marked = 1
    while auxlist <> []:
        u = auxlist.pop( 0 )
        for neighbor in G[u]:
            if color[neighbor] == 'white':
                color[neighbor] = 'gray'
                depth[neighbor] = depth[u] + 1
                parent[neighbor] = u
                auxlist.append( neighbor )
                total_marked += 1
        color[u] = 'black'
    return total_marked, parent, depth

def path( G, v1, v2, parent ):
	if v1 == v2:
		return v1
	elif parent[v2] == None:
		pass
	else:
		aux.append( v2 )
		return path( G, v1, parent[v2], parent )

def result( G, aux ):
	if li == 0 and pi == 0 and aux[4] == 1:
		return G
	auxAux = ()
	if aux[4] == 0:
		if li >= 2 and ( ld + 2 <= pd or pd == 0 ):
			auxAux = ( li - 2, ld + 2, pi, pd, 1 )
			make_link( G, aux, auxAux )
			result( G, auxAux )
		if li >= 1 and pi >= 1 and ld + 1 <= pd + 1:
			auxAux = ( li - 1, ld + 1, pi - 1, pd + 1, 1 )
			make_link( G, aux, auxAux )
			result( G, auxAux )
		if pi >= 2 and pd + 2 >= ld:
			auxAux = ( li, ld, pi - 2, pd + 2, 1 )
			make_link( G, aux, auxAux )
			result( G, auxAux )
	else:
		auxAux = ( li + 1, ld - 1, pi, pd, 0 )
		make_link( G, aux, auxAux )
		result( G, auxAux )
		if pd - 1 >= ld or pd - 1 == 0:
			auxAux = ( li, ld, pi + 1, pd - 1, 0 )
			make_link( G, aux, auxAux )
			result( G, auxAux )

t = int( sys.stdin.readline() )

while t > 0:
	n, m, p, q = map( int, sys.stdin.readline().split() )
	if ( p != 0 and n > p ) or ( q != 0 and m > q ):
		print -1
	else:
		G = {}
		tupleI = ( n, m, p, q, 0 )
		tupleF = ( 0, n + m, 0, p + q, 1 )
		result( G, tupleI )
		if len( G ) > 0:
			parent = BFS_iterative( G, tupleI )[1]
			path( G, tupleI, tupleF, parent )
			print len( aux )
		else:
			print len( G )

	aux = []
	t -= 1"""

queue = []

def BFS( node ):
	queue.append( node )
	count = 0

	while( len( queue ) > 0 ):
		aux = queue.pop( 0 )

		li, ld, pi, pd = aux[0], aux[1], aux[2], aux[3]

		if li == 0 and pi == 0:
			return aux[5]

		if aux[4] == 0:
			if pi >= 2 and pd + 2 >= ld and ( pi - 2 >= li or pi - 2 == 0 ):
				nodeAux = ( li, ld, pi - 2, pd + 2, 1, aux[5] + 1 )
				queue.append( nodeAux )
			elif li >= 2 and ( ld + 2 <= pd or pd == 0 ) and ( li - 2 <= pi or pi == 0 ):
				nodeAux = ( li - 2, ld + 2, pi, pd, 1, aux[5] + 1 )
				queue.append( nodeAux )
			elif li >= 1 and pi >= 1 and ld + 1 <= pd + 1 and ( li - 1 <= pi - 1 or pi - 1 == 0 ):
				nodeAux = ( li - 1, ld + 1, pi - 1, pd + 1, 1, aux[5] + 1 )
				queue.append( nodeAux )
			elif pi >= 1 and ( pi - 1 >= li or pi - 1 == 0 ) and pd + 1 >= ld:
				nodeAux = ( li, ld, pi - 1, pd + 1, 1, aux[5] + 1 )
				queue.append( nodeAux )
			elif li >= 1 and ( li - 1 <= pi or pi == 0 ) and ( ld + 1 <= pd or pd == 0 ):
				nodeAux = ( li - 1, ld + 1, pi, pd, 1, aux[5] + 1 )
				queue.append( nodeAux )
		else:
			if pd >= 1 and ( pd - 1 >= ld or pd - 1 == 0 ) and pi + 1 >= li:
				nodeAux = ( li, ld, pi + 1, pd - 1, 0, aux[5] + 1 )
				queue.append( nodeAux )
			elif ld >= 1 and ( ld - 1 <= pd or pd == 0 ) and ( li + 1 <= pi or pi == 0 ):
				nodeAux = ( li + 1, ld - 1, pi, pd, 0, aux[5] + 1 )
				queue.append( nodeAux )
			elif ld >= 2 and ( li + 2 <= pi or pi == 0 ) and ( ld - 2 <= pd or pd == 0 ):
				nodeAux = ( li + 2, ld - 2, pi, pd, 0, aux[5] + 1 )
				queue.append( nodeAux )
			elif ld >= 1 and pd >= 1 and li + 1 <= pi + 1 and ( ld - 1 <= pd - 1 or pd - 1 == 0 ):
				nodeAux = ( li + 1, ld - 1, pi + 1, pd - 1, 0, aux[5] + 1 )
				queue.append( nodeAux )
			elif pd >= 2 and pi + 2 >= li and ( pd - 2 >= ld or pd - 2 == 0 ):
				nodeAux = ( li, ld, pi + 2, pd - 2, 0, aux[5] + 1 )
				queue.append( nodeAux )
			"""if pd - 1 >= ld or pd - 1 == 0:
				nodeAux = ( li, ld, pi + 1, pd - 1, 0, aux[5] + 1 )
				queue.append( nodeAux )
			elif ( ld - 1 <= pd or pd == 0 ) and ( li + 1 <= pi or pi == 0 ):
				nodeAux = ( li + 1, ld - 1, pi, pd, 0, aux[5] + 1 )
				queue.append( nodeAux )
			elif li + 1 <= pi + 1:
				nodeAux = ( li + 1, ld - 1, pi + 1, pd - 1, 0, aux[5] + 1 )
				queue.append( nodeAux )"""


t = int( sys.stdin.readline() )

while t > 0:
	n, m, p, q = map( int, sys.stdin.readline().split() )
	if ( p != 0 and n > p ) or ( q != 0 and m > q ):
		print -1
	else:
		print BFS( ( n, m, p, q, 0, 0 ) )		

	t -= 1