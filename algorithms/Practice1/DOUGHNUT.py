import sys
 
n = int( sys.stdin.readline() )
 
while n > 0:
	a = map( int, sys.stdin.readline().split() )
	if a[0] * a[2] <= a[1]:
		print "yes"
	else:
		print "no"
	n -= 1 