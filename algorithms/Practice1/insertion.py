import sys
import random
import time

def isOrder( array ):
	aux = array[0]
	for i in xrange( 1, len( array ) ):
		if aux <= array[i]:
			aux = array[i]
		else:
			return False
	return True

#array = [5, 2, 4, 6, 1, 3]

n = 1000

array = []

for i in xrange( 1, n + 1 ):
	#array.append( int( sys.stdin.readline() ) )
	array.append( i )

random.shuffle( array )

startTime = time.clock()

for i in xrange( 1, len( array ) ):
	key = array[i]
	j = i - 1
	while j >= 0 and key < array[j]:
		array[j + 1] = array[j]
		j -= 1
	array[j + 1] = key
	i += 1

finishTime = time.clock() - startTime

print finishTime