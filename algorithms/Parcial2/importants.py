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

def makeLink( G, u, v, weight ):
	if u not in G:
		G[u] = {}
	G[u][v] = weight

##### ------------ DJIKSTRA --------------##########

def father( i ):
	if( i % 2 == 0 ):
		return i / 2 - 1
	return i / 2

def leftChildren( i ):
	return 2 * i + 1

def rightChildren( i ):
	return 2 * i + 2

def push( heap, distances, vertex ):
	heap.append( vertex )
	i = len( heap ) - 1
	while( father( i ) >= 0 ):
		if( distances[heap[i]] < distances[heap[father( i )]] ):
			( heap[i], heap[father( i )] ) = ( heap[father( i )], heap[i] )
			i -= 1
		else:
			break

def pop( distances, heap ):
	minim = heap[0]
	heap[0] = heap[len( heap ) - 1]
	del heap[len( heap ) - 1]
	i = 0
	while( i < len( heap ) ):
		if( rightChildren( i ) < len( heap ) and min( distances[heap[leftChildren( i )]], distances[heap[rightChildren( i )]] ) < distances[heap[i]] ):
			if( distances[heap[leftChildren( i )]] < distances[heap[rightChildren( i )]] ):
				( heap[i], heap[leftChildren( i )] ) = ( heap[leftChildren( i )], heap[i] )
			else:
				( heap[i], heap[rightChildren( i )] ) = ( heap[rightChildren( i )], heap[i] )
			i += 1
		elif( leftChildren( i ) < len( heap ) and distances[heap[leftChildren( i )]] < distances[heap[i]] ):
			( heap[i], heap[leftChildren( i )] ) = ( heap[leftChildren( i )], heap[i] )
			i += 1
		else:
			break
	return minim

def makeLink( G, u, v, weight ):
	if u not in G:
		G[u] = {}
	G[u][v] = weight

def dijkstra( G, t, v ):
	distances = {}
	heap = [v]
	for vertex1 in G:
		if vertex1 == v:
			distances[v] = 0
		elif( vertex1 not in heap ):
			distances[vertex1] = float( 'Inf' )
			heap.append( vertex1 )
		else:
			continue
		for vertex2 in G[vertex1]:
			if vertex2 == v:
				continue
			elif( vertex2 not in heap ):
				distances[vertex2] = float( 'Inf' )
				heap.append( vertex2 )
	while len( heap ) > 0:
		u = pop( distances, heap )
		if u in G:
			for vertex in G[u]:
				if( distances[vertex] > distances[u] + G[u][vertex] ):
					distances[vertex] = distances[u] + G[u][vertex]
					t[vertex] = u
					aux = heap[:]
					for x in aux:
						push( heap, distances, x )

	return distances, t

G = {}
d = {}
t = {}
t[0] = None

while True:
	s, f, w = map( int, sys.stdin.readline().split() )
	if s == 0 and f == 0:
		break
	makeLink( G, s, f, w )

print dijkstra( G, t, 0 )

######### ------------ BELLMAN-FORD ---------------- ############

def initializeSingleSource( G, d, t, s ):
	for v in G.keys():
		for w in G[v]:
			d[w] = float( 'Inf' )
			t[w] = None
		d[v] = float( 'Inf' )
		t[v] = None
	d[s] = 0

def relax( G, d, t, u, v ):
	if d[v] > d[u] + G[u][v]:
		d[v] = d[u] + G[u][v]
		t[v] = u

def bellmanFord( G, d, t, s ):
	initializeSingleSource( G, d, t, s )
	for i in xrange( len( d ) - 1 ):
		for v1 in G:
			for v2 in G[v1]:
				relax( G, d, t, v1, v2 )
	for v1 in G:
		for v2 in G[v1]:
			if d[v2] > d[v1] + G[v1][v2]:
				return False
	return True

######### ------------ FLOYD-WARSHALL ---------------- ############
def floydWarshall( w ):
	n = len( w )
	d = w[:]
	for j in xrange( n ):
		print d[j]
	for i in xrange( n ):
		print
		for j in xrange( n ):
			for k in xrange( n ):
				d[j][k] = min( d[j][k], d[j][i] + d[i][k] )
		for j in xrange( n ):
			print d[j]
	return d

n = 10
w = []
for i in xrange( n ):
	w.append( [10000 for j in xrange( 10 )] )

for i in xrange( n ):
	for j in xrange( n ):
		if i == j:
			w[i][j] = 0

while True:
	s, f, weight = map( int, sys.stdin.readline().split() )
	if s == 0 and f == 0:
		break
	w[s - 1][f - 1] = weight

floydWarshall( w )

############# --------------- LCS -------------------################

sys.setrecursionlimit( 1000000000 )

def LCS( word1, word2 ):
    m = len( word1 )
    n = len( word2 )
    aux = [[0] * ( n + 1 ) for i in xrange( m + 1 )]
    for i in xrange( 1, m + 1 ):
        for j in xrange( 1, n + 1 ):
            if word1[i - 1] == word2[j - 1]: 
                aux[i][j] = aux[i - 1][j - 1] + 1
            else:
                aux[i][j] = max( aux[i][j - 1], aux[i - 1][j] )
    return aux

def allSubsequences( aux, word1, word2, i, j ):
    if i == 0 or j == 0:
        return set( [""] )
    elif word1[i - 1] == word2[j - 1]:
        return set( [x + word1[i - 1] for x in allSubsequences( aux, word1, word2, i - 1, j - 1 )] )
    else:
        result = set()
        if aux[i][j - 1] >= aux[i - 1][j]:
            result.update( allSubsequences( aux, word1, word2, i, j - 1 ) )
        if aux[i - 1][j] >= aux[i][j - 1]:
            result.update( allSubsequences( aux, word1, word2, i - 1, j ) )
        return result

t = int( sys.stdin.readline() )

for k in xrange( t ):
	print "Case #" + str( k + 1 ) + ":"
	word1 = sys.stdin.readline().strip()
	word2 = sys.stdin.readline().strip()
	aux = LCS( word1, word2 )
	result = allSubsequences( aux, word1, word2, len( word1 ), len( word2 ) )
	if len( result ) == 1 and list( result )[0] == "":
		print -1
	else:
		for x in sorted( result ):
			print x

############## -------------- LCSubstring ---------------------- ############

def fillTable( table, m, n ):
	for i in xrange( m ):
		aux = []
		for j in xrange( n ):
			aux.append( 0 )
		table.append( aux )

def LCS( word1, word2 ):
	m = len( word1 )
	n = len( word2 )
	marks, results = [], []
	fillTable( marks, m, n )
	fillTable( results, m + 1, n + 1 )
	maxim = 0
	for i in xrange( 1, m + 1 ):
		for j in xrange( 1, n + 1 ):
			if word1[i - 1] == word2[j - 1]:
				results[i][j] = results[i - 1][j - 1] + 1
				if results[i][j] > maxim:
					maxim = results[i][j]
			else:
				results[i][j] = 0
	return maxim

t = int( sys.stdin.readline() )
temp = []

for k in xrange( t ):
	word1 = sys.stdin.readline().strip()
	word2 = sys.stdin.readline().strip()
	print LCS( word1, word2 )

################ -------------- Money -----------------################

sys.setrecursionlimit( 100000000 )
coinValue = []
memo = {}

def change( n, coinValue ):
	if n < 0:
		return 10000
	if n == 0:
		return 0

	temp = []
	for i in xrange( len( coinValue ) ):
		value = n - coinValue[i]
		if value not in memo:
			aux = change( value, coinValue )
			memo[value] = aux
		else:
			aux = memo[value]
		temp.append( aux )
	minim = min( temp )
	return 1 + minim

t = int( sys.stdin.readline() )

while t > 0:
	memo = {}
	n, m = map( int, sys.stdin.readline().split() )
	coinValue = map( int, sys.stdin.readline().split() )
	result = change( n, coinValue )
	if result == 0 or result > 1000:
		print -1
	else:
		print result
	t -= 1

################## ------------ ROUND --------------------####

a = 2
b = 3
round (a*1.0/b,2)
#0.67000000000000004
print '%.2f' % round (a*1.0/b,2)
#0.67

################# ----------- MATRIX ---------------###########

n = 10
w = []
for i in xrange( n ):
	w.append( [10000 for j in xrange( 10 )] )

for i in xrange( n ):
	for j in xrange( n ):
		if i == j:
			w[i][j] = 0