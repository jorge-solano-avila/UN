import sys

def make_link( G, node1, node2 ):
    if node1 not in G:
        G[node1] = {}
    ( G[node1] )[node2] = 1
    if node2 not in G:
        G[node2] = {}
    ( G[node2] )[node1] = 1
    return G

def result( G, node ):
    color = {}
    depth = {}
    queue = []
    queue.append( node )
    depth[node] = 0
    color[node] = 'white'

    matrixR = "11111", "01111", "00.11", "00001", "00000"

    while( len( queue ) > 0 ):
        aux = queue.pop( 0 )

        temp1, temp2 = 0, 0
        for i in xrange( 5 ):
            temp2 = aux[i].find( '.' )
            temp1 = i
            if temp2 != -1:
                break
        if temp1 - 2 >= 0 and temp2 - 1 >= 0:
            matrixAux = list( aux )[:]
            for i in xrange( 5 ):
                string = ""
                for j in xrange( 5 ):
                    if i == temp1 - 2:
                        if j == temp2 - 1:
                            string += '.'
                        else:
                            string += aux[i][j]
                    elif i == temp1:
                        if j == temp2:
                            string += aux[temp1 - 2][temp2 - 1]
                        else:
                            string += aux[i][j]
                if i == temp1 - 2:
                    matrixAux[temp1 - 2] = string
                elif i == temp1:
                    matrixAux[temp1] = string
            matrixAux = tuple( matrixAux )
            if not matrixAux in G:
                queue.append( matrixAux )
                make_link( G, aux, matrixAux ) 
                depth[matrixAux] = depth[aux] + 1
            if depth[matrixAux] > 10:
                return -1
            if matrixAux == matrixR:
                return depth[matrixR]
        if temp1 - 2 >= 0 and temp2 + 1 <= 4:
            matrixAux = list( aux )[:]
            for i in xrange( 5 ):
                string = ""
                for j in xrange( 5 ):
                    if i == temp1 - 2:
                        if j == temp2 + 1:
                            string += '.'
                        else:
                            string += aux[i][j]
                    elif i == temp1:
                        if j == temp2:
                            string += aux[temp1 - 2][temp2 + 1]
                        else:
                            string += aux[i][j]
                if i == temp1 - 2:
                    matrixAux[temp1 - 2] = string
                elif i == temp1:
                    matrixAux[temp1] = string
            matrixAux = tuple( matrixAux )
            if not matrixAux in G:
                queue.append( matrixAux )
                make_link( G, aux, matrixAux ) 
                depth[matrixAux] = depth[aux] + 1
            #print depth[matrixAux]
            if depth[matrixAux] > 10:
                return -1
            if matrixAux == matrixR:
                return depth[matrixR]
        if temp1 - 1 >= 0 and temp2 - 2 >= 0:
            matrixAux = list( aux )[:]
            for i in xrange( 5 ):
                string = ""
                for j in xrange( 5 ):
                    if i == temp1 - 1:
                        if j == temp2 - 2:
                            string += '.'
                        else:
                            string += aux[i][j]
                    elif i == temp1:
                        if j == temp2:
                            string += aux[temp1 - 1][temp2 - 2]
                        else:
                            string += aux[i][j]
                if i == temp1 - 1:
                    matrixAux[temp1 - 1] = string
                elif i == temp1:
                    matrixAux[temp1] = string
            matrixAux = tuple( matrixAux )
            if not matrixAux in G:
                queue.append( matrixAux )
                make_link( G, aux, matrixAux ) 
                depth[matrixAux] = depth[aux] + 1
            #print depth[matrixAux]
            if depth[matrixAux] > 10:
                return -1
            if matrixAux == matrixR:
                return depth[matrixR]
        if temp1 - 1 >= 0 and temp2 + 2 <= 4:
            matrixAux = list( aux )[:]
            for i in xrange( 5 ):
                string = ""
                for j in xrange( 5 ):
                    if i == temp1 - 1:
                        if j == temp2 + 2:
                            string += '.'
                        else:
                            string += aux[i][j]
                    elif i == temp1:
                        if j == temp2:
                            string += aux[temp1 - 1][temp2 + 2]
                        else:
                            string += aux[i][j]
                if i == temp1 - 1:
                    matrixAux[temp1 - 1] = string
                elif i == temp1:
                    matrixAux[temp1] = string
            matrixAux = tuple( matrixAux )
            if not matrixAux in G:
                queue.append( matrixAux )
                make_link( G, aux, matrixAux ) 
                depth[matrixAux] = depth[aux] + 1
            #print depth[matrixAux]
            if depth[matrixAux] > 10:
                return -1
            if matrixAux == matrixR:
                return depth[matrixR]
        if temp1 + 2 <= 4 and temp2 - 1 >= 0:
            matrixAux = list( aux )[:]
            for i in xrange( 5 ):
                string = ""
                for j in xrange( 5 ):
                    if i == temp1 + 2:
                        if j == temp2 - 1:
                            string += '.'
                        else:
                            string += aux[i][j]
                    elif i == temp1:
                        if j == temp2:
                            string += aux[temp1 + 2][temp2 - 1]
                        else:
                            string += aux[i][j]
                if i == temp1 + 2:
                    matrixAux[temp1 + 2] = string
                elif i == temp1:
                    matrixAux[temp1] = string
            matrixAux = tuple( matrixAux )
            if not matrixAux in G:
                queue.append( matrixAux )
                make_link( G, aux, matrixAux ) 
                depth[matrixAux] = depth[aux] + 1
            #print depth[matrixAux]
            if depth[matrixAux] > 10:
                return -1
            if matrixAux == matrixR:
                return depth[matrixR]
        if temp1 + 2 <= 4 and temp2 + 1 <= 4:
            matrixAux = list( aux )[:]
            for i in xrange( 5 ):
                string = ""
                for j in xrange( 5 ):
                    if i == temp1 + 2:
                        if j == temp2 + 1:
                            string += '.'
                        else:
                            string += aux[i][j]
                    elif i == temp1:
                        if j == temp2:
                            string += aux[temp1 + 2][temp2 + 1]
                        else:
                            string += aux[i][j]
                if i == temp1 + 2:
                    matrixAux[temp1 + 2] = string
                elif i == temp1:
                    matrixAux[temp1] = string
            matrixAux = tuple( matrixAux )
            if not matrixAux in G:
                queue.append( matrixAux )
                make_link( G, aux, matrixAux ) 
                depth[matrixAux] = depth[aux] + 1
            #print depth[matrixAux]
            if depth[matrixAux] > 10:
                return -1
            if matrixAux == matrixR:
                return depth[matrixR]
        if temp1 + 1 <= 4 and temp2 - 2 >= 0:
            matrixAux = list( aux )[:]
            for i in xrange( 5 ):
                string = ""
                for j in xrange( 5 ):
                    if i == temp1 + 1:
                        if j == temp2 - 2:
                            string += '.'
                        else:
                            string += aux[i][j]
                    elif i == temp1:
                        if j == temp2:
                            string += aux[temp1 + 1][temp2 - 2]
                        else:
                            string += aux[i][j]
                if i == temp1 + 1:
                    matrixAux[temp1 + 1] = string
                elif i == temp1:
                    matrixAux[temp1] = string
            matrixAux = tuple( matrixAux )
            if not matrixAux in G:
                queue.append( matrixAux )
                make_link( G, aux, matrixAux ) 
                depth[matrixAux] = depth[aux] + 1
            #print depth[matrixAux]
            if depth[matrixAux] > 10:
                return -1
            if matrixAux == matrixR:
                return depth[matrixR]
        if temp1 + 1 <= 4 and temp2 + 2 <= 4:
            matrixAux = list( aux )[:]
            for i in xrange( 5 ):
                string = ""
                for j in xrange( 5 ):
                    if i == temp1 + 1:
                        if j == temp2 + 2:
                            string += '.'
                        else:
                            string += aux[i][j]
                    elif i == temp1:
                        if j == temp2:
                            string += aux[temp1 + 1][temp2 + 2]
                        else:
                            string += aux[i][j]
                if i == temp1 + 1:
                    matrixAux[temp1 + 1] = string
                elif i == temp1:
                    matrixAux[temp1] = string
            matrixAux = tuple( matrixAux )
            if not matrixAux in G:
                queue.append( matrixAux )
                make_link( G, aux, matrixAux ) 
                depth[matrixAux] = depth[aux] + 1
            #print depth[matrixAux]
            if depth[matrixAux] > 10:
                return -1
            if matrixAux == matrixR:
                return depth[matrixR]

        """for neighbor in G[aux]:
            if neighbor == matrixR:
                return depth[aux] + 1
            if depth[aux] > 10:
                return -1
            if color[neighbor] == 'white':
                color[neighbor] = 'gray'
                depth[neighbor] = depth[aux] + 1
            if depth[neighbor] > 10:
                return -1
        color[aux] = 'black'

        if depth[aux] > 10:
            return -1

        if aux == matrixR:
            return depth[matrixR]"""

t = int( sys.stdin.readline() )

while t > 0:
    matrix = []
    for i in xrange( 5 ):
        matrix.append( sys.stdin.readline().strip() )
    matrix = tuple( matrix )
    G = {}
    #matrixR = "11111", "01111", "00.11", "00001", "00000"
    depth = result( G, matrix )
    if depth == -1:
        print "no se puede resolver"
    else:
        print depth
    t -= 1