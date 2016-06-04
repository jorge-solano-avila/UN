import sys

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