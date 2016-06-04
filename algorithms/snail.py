matrix = [	[1, 2, 3, 4], 
			[5, 6, 7, 8], 
			[9, 10, 11, 12], 
			[13, 14, 15, 16]
		]

lenM = len( matrix )

array = []

aux = [x for x in xrange( lenM - 1, 0, -1 )]

x = 0
count = 2
temp = aux[x]

for i in xrange( lenM ):
	for k in xrange( lenM ):
		for j in xrange( lenM - 2 * i ):
			if k == 0:
				if i == 0:
					array.append( matrix[i][j + i] )
				else:
					if count > 0:
						if temp > 0:
							array.append( matrix[i + 1][j + i] )
							temp -= 1
						else:
							temp = aux[x]
							x += 1
							count -= 1
					else:
						count = 2
			elif k == 1:
				if count > 0:
					if temp > 0:
						array.append( matrix[j + i + 1][3 - i] )
						temp -= 1
					else:
						temp = aux[x]
						x += 1
						count -= 1
				else:
					count = 2
			elif k == 2:
				if count > 0:
					if temp > 0:
						array.append( matrix[3 - i][3 - j - i - 1] )
						temp -= 1
					else:
						temp = aux[x]
						x += 1
						count -= 1
				else:
					count = 2
			elif k == 3:
				if count > 0:
					if temp > 0:
						array.append( matrix[3 - j - i - 1][i] )
						temp -= 1
					else:
						temp = aux[x]
						x += 1
						count -= 1
				else:
					count = 2

print array