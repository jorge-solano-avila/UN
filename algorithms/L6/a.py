import sys

array = []

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

def connected_components( G ):
    color = {}
    for v in G:
        color[v] = 'white'
    count = 0
    for v in G:
        if color[v] == 'white':
            count += 1
            array.append( DFS_Visit( G, v, color ) )
    return count

line = map( int, sys.stdin.readline().split() )
n, m = line[0], line[1]
edges = []
G = {}
while m > 0:
    edges.append( map( int, sys.stdin.readline().split() ) )
    m -= 1

for v1, v2 in edges:
    make_link( G, v1, v2 )

numbers = [x for x in xrange( n )]

count = 0
flag = False

connected_components( G )

for number in numbers:
    for item in edges:
        for j in xrange( 2 ):
            if number == item[j]:
                flag = True
                break
        if flag:
            break
    if not flag:
        count += 1
    flag = False

for i in xrange( count ):
    array.append( 1 )

solu = 0

for i in xrange( len( array ) ):
    for j in xrange( len( array ) ):
        if i == j:
            continue
        solu += array[i] * array[j]
print solu / 2