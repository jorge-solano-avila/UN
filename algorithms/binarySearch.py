import sys

array = [1, 2, 3, 4, 5, 6]

def binarySearch( num ):
	low = 0
	high = len( array ) - 1
	while low <= high:
		mid = low + ( high - low ) / 2
		if array[mid] == num:
			return mid
		elif array[mid] < num:
			low = mid + 1
		else:
			high = mid - 1
	return -1

print binarySearch( 6 )