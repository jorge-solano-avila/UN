import sys
import random

sys.setrecursionlimit( 100000 )

def DFS_Visit( G, node, color ):
	color[node] = 'gray'
	total_marked = 1
	for neighbor in G[node]:
		if color[neighbor] == 'white':
			total_marked += DFS_Visit( G, neighbor, color )
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

n = int( sys.stdin.readline().strip() )

while n > 0:
	G = {}
	edges = []

	a = map( int, sys.stdin.readline().split() )
	for i in xrange( a[1] ):
		edges.append( map( int, sys.stdin.readline().split() ) )
	b = map( int, sys.stdin.readline().split() )

	for v1, v2 in edges:
		make_link( G, v1, v2 )
	
	color = {}
	for v in G:
		color[v] = 'white'

	count = DFS_Visit( G, b[0], color )
	
	print ( a[0] - count ) * b[1]
	
	n -=1