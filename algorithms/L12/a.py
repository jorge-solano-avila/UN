import sys

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