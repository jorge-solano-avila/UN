import sys

def add( n ):
	return n * ( n - 1 ) / 2

n = int( sys.stdin.readline() )

while n > 0:
	a = map( float, sys.stdin.readline().split() )
	t = int( a[0] )
	even = 0
	odd = 0
	if t % 2 == 0:
		even = t / 2
		odd = t - even
	else:
		even = t / 2 + 1
		odd = t - even
	count = 0
	if a[1] == a[2] and a[2] == a[3]:
		print int( add( t ) * a[1] )
	else:
		count += add( even ) * a[1]
		count += ( add( t ) - add( even ) - add( odd ) ) * a[2]
		count += add( odd ) * a[3]
		print int( count )
	n -= 1