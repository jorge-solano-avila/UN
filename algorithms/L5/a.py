import sys
import math

array = sys.stdin.readlines()

for item in array:
	a = item.split()
	if a[0] == "chain":
		print int( a[1] ) - 1
	elif a[0] == "ring":
		print int( a[1] )
	elif a[0] == "grid":
		print int ( 2 * int( a[1] ) - 2 * math.sqrt( int( a[1] ) ) )
	elif a[0] == "complete":
		print int( a[1] ) * ( int( a[1] ) - 1 ) / 2 