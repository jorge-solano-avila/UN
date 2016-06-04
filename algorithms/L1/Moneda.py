import sys

t = int( raw_input() )

for i in xrange( t ):
	n = int( raw_input() )
	a = map( int, sys.stdin.readline().split() )
	aux = 1
	for k in a:
		if k == 1:
			aux = -1
			break
	print aux