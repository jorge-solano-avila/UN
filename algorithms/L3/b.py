import sys

n = int( sys.stdin.readline() )

while n > 0:
	a = map( int, sys.stdin.readline().split() )
	if a[0] == 1:
		if a[1] > 1:
			print a[1] ** 3 + 2 * ( a[1] ** 2 ) + 2 * a[1] - 1
		else:
			print 4
	else:
		print 4 + 3 * ( a[1] ** 2 )
	n -= 1; 