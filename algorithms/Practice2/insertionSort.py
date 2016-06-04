import itertools
import time

def merge( array, l, m, u ):
	array1 = array[l:m + 1] + [float( "INF" )]
	array2 = array[m + 1:u + 1] + [float( "INF" )]
	i = 0
	j = 0
	for k in xrange( l, u + 1 ):
		if array1[i] <= array2[j]:
			array[k] = array1[i]
			i += 1
		else:
			array[k] = array2[j]
			j += 1 

def mergeSort( array, l, u ):
	if l < u:
		m = ( l + u ) / 2
		mergeSort( array, l, m )
		mergeSort( array, m + 1, u )
		merge( array, l, m, u ) 

def insertionSort( array ):
	for i in xrange( 1, len( array ) ):
		key = array[i]
		j = i - 1
		while( j >= 0 and key < array[j] ):
			array[j + 1] = array[j]
			array[j] = key
			j -= 1

def calculateTime( array ):
	totalTime = 0
	for i in xrange( 100 ):
		initial = time.time()
		insertionSort( array, 0, len( array ) - 1 )
		result = time.time() - initial
		totalTime += result
	return totalTime / 100

array = []
times = []
aux = []
"""
for i in xrange( 4, 7 ):
	array = []
	for j in xrange( i ):
		array.append( j + 1 )

	aux.append( calculateTime( array ) )

times.append( aux )
aux = []
"""
for i in xrange( 4, 7 ):
	array = []
	for j in xrange( i ):
		array.append( j + 1 )
	array = list( itertools.permutations( array, i ) )
	factorial = len( array )
	
	totalTime = 0
	for j in xrange( factorial ):
		totalTime += calculateTime( list( array[j] ) )
	totalTime /= factorial

	aux.append( totalTime )

times.append( aux )
aux = []
print times
"""
for i in xrange( 4, 7 ):
	array = []
	for j in xrange( i - 1, -1, -1 ):
		array.append( j + 1 )

	aux.append( calculateTime( array ) )

times.append( aux )

print times
"""