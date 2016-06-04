import sys

def binarySearch( array, num ):
	low = 0
	high = len( array ) - 1
	while low < high:
		mid = low + ( high - low ) / 2
		if array[mid] > num:
			high = mid
		else:
			low = mid + 1
	if array[low] <= num:
		return low + 1
	return low

t = int( sys.stdin.readline().strip() )

while( t > 0 ):
	a = map( int, sys.stdin.readline().strip().split() )
	array1 = map( int, sys.stdin.readline().strip().split() )
	array2 = map( int, sys.stdin.readline().strip().split() )

	array1.sort()

	for i in xrange( len( array2 ) ):
		if i == len( array2 ) - 1:
			print binarySearch( array1, array2[i] )
		else:
			print binarySearch( array1, array2[i] ),
	t -= 1