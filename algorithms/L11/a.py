import sys
#import time

total = {}

def pow( base, pot ):
	result = 1
	while( pot > 0 ):
		if( pot % 2 == 1 ):
			result *= base
		result **= 2
		pot /= 2
	return result 

def function( base ):
	f = {}
	for j in xrange( len( base ) ):
		f[j] = base[j]
	k = 0
	while( True ):
		add = 0
		for j in xrange( len( f ) - 1, -1 + k, -1 ):
			add += f[j]
		#print len( str( add ) )
		if len( str( add ) ) < MAX:
			f[len( f )] = add
		else:
			return len( f )
		k += 1

#initial = time.time()
n = int( sys.stdin.readline().strip() )
MAX = 101

for i in xrange( n ):
	base = map( int, sys.stdin.readline().split() )
	if tuple( base ) not in total:
		result = function( base )
		total[tuple( base )] = result
	print total[tuple( base )]
#print time.time() - initial