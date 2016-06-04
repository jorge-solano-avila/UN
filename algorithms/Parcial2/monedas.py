import sys

def change(bill, coins):
    total = [0] * (bill + 1)
    total[0] = 1
    for c in coins:
        for j in xrange(c , bill + 1):
            total[j] += total[j - c]
    #print total
    return total[bill]

cases = int( sys.stdin.readline( ) )

for i in range(cases):
	nm = sys.stdin.readline( ).strip().split()
	bill = int(nm[0])
	nc = int(nm[1])
	coins = map(int, sys.stdin.readline( ).strip( ).split( ) )
	ans = change(bill, coins)
	print ans