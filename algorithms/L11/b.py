import sys
#import time

sys.setrecursionlimit( 10000 )
MOD = 9999959999

total = []
total.append( range( 1, 2002 ) )
for i in xrange( 1000 ):
	temp = []
	for j in xrange( 2001 ):
		temp.append( 0 )
	total.append( temp[:] )

def calculate( array ):
	l = array[0]
	s = array[1]
	if s - 1 >= 0 and s + 1 <= 2000:
		aux1, aux2 = 0, 0
		if total[l - 1][s + 1] != 0 and total[l][s - 1] != 0:
			aux1 = total[l - 1][s + 1]
			aux2 = total[l][s - 1]
		elif total[l - 1][s + 1] != 0:
			aux1 = total[l - 1][s + 1]
			aux2 = calculate( [l, s - 1] )
		elif total[l][s - 1] != 0:
			aux1 = calculate( [l - 1, s + 1] )
			aux2 = total[l][s - 1]
		else:
			aux1 = calculate( [l - 1, s + 1] )
			aux2 = calculate( [l, s - 1] )
		total[l][s] = ( aux1 + aux2 + 1 ) % MOD
	else:
		aux = 0
		if total[l - 1][s + 1] != 0:
			aux = total[l - 1][s + 1]
		else:
			aux = calculate( [l - 1][s + 1] )
		total[l][s] = ( aux + 1 ) % MOD
	return total[l][s]

#initial = time.time()
n = int( sys.stdin.readline() )

while n > 0:
	array = map( int, sys.stdin.readline().split() )
	if total[array[0]][array[1]] == 0:
		calculate( array )
	print total[array[0]][array[1]]
	n -= 1

#print time.time() - initial