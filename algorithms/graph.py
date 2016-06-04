#If you don't have graphviz, you can remove this cell and eliminate all calls to the functions in it.

#from graphviz import Graph, Digraph
#from IPython.display import display

# This function allows to drwaw a graph. It requires graphviz to be installed
"""def display_graph( G, color = {} ):
        dot = Graph( graph_attr = { 'size' : '3.5' } )
        for node in G:
            if not node in color or color[node] == 'white':
                dot.node(node)
            else:
                if color[node] == 'black':
                    dot.node( node, style = 'filled', color = color[node], fontcolor = 'white' )
                else:
                    dot.node( node, style = 'filled', color = color[node] )
        for n1 in G:
            for n2 in G[n1]:
                if n1 < n2:
                    dot.edge( n1, n2 )
        display( dot )"""

# This function allows to draw a search tree. It requires graphviz to be installed
"""def display_parent( prnt ):
        dot = Digraph( graph_attr = { 'size' : '2.5'} )
        for n1 in prnt:
            if prnt[n1] <> None:
                for n2 in prnt[n1]:
                    dot.edge( n2, n1 )
        display( dot )"""

def DFS_Visit( G, node, color ):
    color[node] = 'gray'
    total_marked = 1
#   print "node=", node, ">>> "
#   display_graph(G, color)
    for neighbor in G[node]:
        if color[neighbor] == 'white':
            total_marked += DFS_Visit( G, neighbor, color )
    color[node] = 'black'
#   print "node=", node, "<<< "
#   display_graph(G, color)
    return total_marked

# Graph construction

def make_link( G, node1, node2 ):
    if node1 not in G:
        G[node1] = {}
    ( G[node1] )[node2] = 1
    if node2 not in G:
        G[node2] = {}
    ( G[node2] )[node1] = 1
    return G

def connected_components( G ):
    color = {}
    for v in G:
        color[v] = 'white'
    count = 0
    for v in G:
        print 'v = ', v 
        if color[v] == 'white':
            count += 1
            DFS_Visit( G, v, color )
            #display_graph( G, color )
    return count

def connected( G, v1, v2 ):
    color = {}
    for v in G1:
        color[v] = 'white'
    DFS_Visit( G, v1, color )
    return color[v2] == 'black'

def DFS_Visit_p( G, node, color, parent ):
    color[node] = 'gray'
    total_marked = 1
    for neighbor in G[node]:
        if color[neighbor] == 'white':
            parent[neighbor] = node
            total_marked += DFS_Visit_p( G, neighbor, color, parent )
    color[node] = 'black'
    return total_marked

def path( G, v1, v2 ):
    color = {}
    parent = {}
    for v in G:
        color[v] = 'white'
        parent[v] = None
    DFS_Visit_p( G, v1, color, parent )
    #display_parent( parent )
    node = v2
    pathlist = [node]
    while node <> None:
        node = parent[node]
        #print 'node = ', node
        if node <> None:
            pathlist = [node] + pathlist
    if color[v2] == 'black':
        return pathlist # los vertices en pathlist estan en orden inverso, [::-1] los invierte
    else:
        return []

def DFS_iterative( G, node ):
    color = {}
    parent = {}
    for v in G:
        color[v] = 'white'
    color[node] = 'gray'
    parent[node] = None
    nodelist = [node]
    total_marked = 1
    while nodelist <> []:
        u = nodelist.pop()
        print 'Sale:', u 
        for neighbor in G[u]:
            if color[neighbor] == 'white':
                color[neighbor] = 'gray'
                #print color
                parent[neighbor] = u
                display_parent( parent )
                nodelist.append(neighbor)
                #print 'Pila:', nodelist
                total_marked += 1
        color[u] = 'black'
    return total_marked, parent

def BFS_iterative( G, node ):
    color = {}
    depth = {}
    parent = {}
    for v in G:
        color[v] = 'white'
        depth[v] = float( 'Inf' )
    color[node] = 'gray'
    depth[node] = 0
    parent[node] = None
    nodelist = [node]
    total_marked = 1
    while nodelist <> []:
        u = nodelist.pop(0)
        print 'Sale:', u 
        for neighbor in G[u]:
            if color[neighbor] == 'white':
                color[neighbor] = 'gray'
                depth[neighbor] = depth[u] + 1
                parent[neighbor] = u
                nodelist.append( neighbor )
                #print 'Pila:', nodelist
                total_marked += 1
        color[u] = 'black'
    return total_marked, parent, depth

def DFS_Visit_df( G, node, color, parent, d, f ):
    global time
    time = time + 1
    d[node] = time
    color[node] = 'gray'
    total_marked = 1
    for neighbor in G[node]:
        if color[neighbor] == 'white':
            parent[neighbor] = node
            total_marked += \
                DFS_Visit_df( G, neighbor, color, parent, d, f )
    color[node] = 'black'
    time = time + 1
    f[node] = time
    return total_marked

edges1 = [( 'v', 'r' ), ( 'r', 's' ), ( 'w', 't' ), ( 's','w' ),
         ( 'w', 'x' ), ( 't', 'x' ), ( 't', 'u' ), ( 'x', 'y' ),
         ( 'u', 'y' )]

G1 = { 'y':{} }
for v1, v2 in edges1:
    make_link( G1, v1, v2 )

print G1
#display_graph( G1, {} )

# Initialization of 'color' array
color = {}
for v in G1:
    color[v] = 'white'
    
# Run DFS starting from node 's'
num_nodes = DFS_Visit( G1, 's', color )

print "Number of visited nodes:", num_nodes

print color
#display_graph( G1, color )

print path( G1, 't', 'r' )

"""color = {}
parent = {}
for v in G1:
    color[v] = 'white'
    parent[v] = None

DFS_Visit_p( G1, 's', color, parent )
print parent
#display_parent(parent)"""