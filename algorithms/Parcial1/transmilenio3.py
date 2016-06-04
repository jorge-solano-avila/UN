import sys

sys.setrecursionlimit( 10000000 )

def isCycle( G, v, visited, stack ):
	if not visited[v]:
		visited[v] = True
		stack[v] = True

		if v in G:
			for neighbor in G[v]:
				if not visited[neighbor] and isCycle( G, neighbor, visited, stack ):
					return True
				elif stack[neighbor]:
					return True
	stack[v] = False
	return False

"""
def isCycle( G, n ):e
	nodes = n
	vertex = 0
	for v in G:
		vertex += len( G[v] )
	vertex /= 2
	if vertex < nodes:
		return False
	return True
"""

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
	visited = {}
	stack = {}
	result = {}
	routes = [0 for x in xrange( n )]
	while aux > 0:
		array = map( int, sys.stdin.readline().split() )
		for i in xrange( 1, len( array ) ):
			if i != len( array ) - 1:
				make_link( G, array[i], array[i + 1] )
			visited[array[i]] = False
			stack[array[i]] = False
		aux -= 1
	flag = False
	for v in G:
		if isCycle( G, v, visited, stack ):
			print "Caso %d:" % ( k )
			print "SI"
			flag = True
			break
	if not flag:
		print "Caso %d:" % ( k )
		print "NO"
	k += 1
	t -= 1