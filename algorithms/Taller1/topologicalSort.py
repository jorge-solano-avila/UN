import sys

sys.setrecursionlimit( 10000000 )

topoSort = []
aux = []
G = {}
color = {}

def isCycle( G, n ):
	nodes = n
	vertex = 0
	for v in G:
		vertex += len( G[v] )
	print nodes, vertex
	if vertex < nodes:
		return False
	return True

def make_link( G, node1, node2 ):
	if node1 not in G:
		G[node1] = {}
	( G[node1] )[node2] = 1
	return G

def DFS( G ):
	key = G.keys()
	key.sort()
	for item in key:
		if color[item] == "white":
			DFS_Visit( G, item )

def DFS_Visit( G, node ):
	global topoSort
	global color
	global aux
	color[node] = "black"	
	topoSort.append( node )
	for neighbor in G[node]:
		if neighbor in G:
			DFS_Visit( G, neighbor )
		elif neighbor not in aux:
			aux.append( neighbor )

n, m = map( int, sys.stdin.readline().split() )

while m > 0:
	x, y = map( int, sys.stdin.readline().split() )
	make_link( G, x, y )
	color[x] = "white"
	m -= 1

if isCycle( G, n ):
	print "Sandro fails."
	sys.exit()

DFS( G )
aux.sort()

for i in xrange( 1, n + 1 ):
	if i not in topoSort and i not in aux:
		for j in xrange( len( topoSort ) ):
			if i < topoSort[j]:
				topoSort.insert( j, i )
				break

string = ""
for i in xrange( len( topoSort ) ):
	if i == len( topoSort ) - 1 and len( aux ) == 0:
		string += str( topoSort[i] )
	else:
		string += str( topoSort[i] ) + " "

for i in xrange( len( aux ) ):
	if i == len( aux ) - 1:
		string += str( aux[i] )
	else:
		string += str( aux[i] ) + " "

print string