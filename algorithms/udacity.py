""" UNIT 1 """
def naive(a, b):
    x = a
    y = b
    z = 0
    while x > 0:
        z = z + y
        x = x - 1
    return z

def russian(a, b):
    x = a
    y = b
    z = 0
    while x > 0:
        if x % 2 == 1:
            z = z + y
        y = y << 1
        x = x >> 1
    return z

def rec_russian(a, b):
    if a == 0:
        return 0
    if a % 2 == 0:
        return 2 * rec_russian(a/2, b)
    return b + 2 * rec_russian((a-1)/2, b)

""" UNIT 2 """
############################# Lecture 4: Ring Network ########################

def make_link(G, node1, node2):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = 1
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = 1
    return G

# Make an empty graph
a_ring = {}

n = 5

# Add in the edges
for i in range(n):
    make_link(a_ring, i, (i+1)%n)
# How many nodes? 
print len(a_ring)

# How many edges? 
print sum([len(a_ring[node]) for node in a_ring.keys()])/2

print a_ring

#################### Lecture 5: Grid Network #################

import math
def make_link(G, node1, node2):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = 1
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = 1
    return G

# Make an empty graph
G = {}    

n = 256
side = int(math.sqrt(n))

# Add in the edges
for i in range(side):
    for j in range(side):
        if i < side-1: make_link(G, (i,j), (i+1, j))
        if j < side-1: make_link(G, (i,j), (i, j+1))

# How many nodes? 
print len(G)

# How many edges? 
print sum([len(G[node]) for node in G.keys()])/2

###################### Lecture 16: Complete Graph ############

def make_link(G, node1, node2):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = 1
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = 1
    return G

#
# How many edges in a complete graph on n nodes?
#

def clique(n):
    # Return the number of edges
    # Try to use a mathematical formula...

    # Make an empty graph
    G = {}

    # Add in the edges
    for i in range(n):
        for j in range(n):
            if i<j: make_link(G, i, j)

    return sum([len(G[node]) for node in G.keys()])/2

for n in range(1,10):
    print n, clique(n), n*(n-1)/2

##################### Lecture 21: Recursive Graphs (Pseudo-Code) ###################

def makeG(n):

    if n == 1: return <a single node>

    G1 = makeG(n/2)
    G2 = makeG(n/2)

    i1 = <random node from G1 without replacement>
    i2 = <random node from G2 without replacement>

    make_link(G, i1, i2)

    return G

################################ Lecture 25: Tangled Hypercube (Pseudo-Code) ###############3

def makeG(n):

    if n == 1: return <a single node>

    G1 = makeG(n/2)
    G2 = makeG(n/2)

    i1 = <list of nodes of G1 in random order>
    i2 = <list of nodes of G2 in random order>

    for i in range(n/2):
        make_link(G, i1[i], i2[i])

    return G

""" UNIT 3 """
################## Lecture 5: Clustering Coefficient Code ####################333

def make_link(G, node1, node2):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = 1
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = 1
    return G

flights = [("ORD", "SEA"), ("ORD", "LAX"), ('ORD', 'DFW'), ('ORD', 'PIT'),
          ('SEA', 'LAX'), ('LAX', 'DFW'), ('ATL', 'PIT'), ('ATL', 'RDU'),
          ('RDU', 'PHL'), ('PIT', 'PHL'), ('PHL', 'PVD')]

G = {}
for (x,y) in flights: make_link(G,x,y)

def clustering_coefficient(G,v):
    neighbors = G[v].keys()
    if len(neighbors) == 1: return -1.0
    links = 0
    for w in neighbors:
        for u in neighbors:
            if u in G[w]: links += 0.5
    return 2.0*links/(len(neighbors)*(len(neighbors)-1))

print clustering_coefficient(G,"ORD")

total = 0
for v in G.keys():
    total += clustering_coefficient(G,v)

print total/len(G)

################### Lecture 7: Connected Components Code: ################

connections = [('a', 'g'), ('a', 'd'), ('d', 'g'), ('g', 'c'), ('b', 'f'),
               ('f', 'e'), ('e', 'h')]

G = {}
for (x,y) in connections: make_link(G,x,y)

###################################################################
# Transversal...
#  Call this routine on nodes being visited for the first time
def mark_component(G, node, marked):
    marked[node] = True
    total_marked = 1
    for neighbor in G[node]:
        if neighbor not in marked:
            total_marked += mark_component(G, neighbor, marked)
    return total_marked

def list_component_sizes(G):
    marked = {}
    for node in G.keys():
        if node not in marked:
            print "Component containing", node, ": ", mark_component(G, node, marked)

list_component_sizes(G)
#################### Lecture 9: Checking Pairwise Connectivity (Solution) ################
def mark_component(G, node, marked):
    marked[node] = True
    total_marked = 1
    for neighbor in G[node]:
        if neighbor not in marked:
            total_marked += mark_component(G, neighbor, marked)
    return total_marked

def check_connection(G, v1, v2):
    marked = {}
    mark_component(G, v1, marked)
    return v2 in marked


#################### Lecture 17: BFS Code #############################33
import csv

def make_link(G, node1, node2):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = 1
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = 1
    return G

def read_graph(filename):
    # Read an undirected graph in CSV format. Each line is an edge
    tsv = csv.reader(open(filename), delimiter='\t')
    G = {}
    for (node1, node2) in tsv: make_link(G, node1, node2)
    return G

# Read the marvel comics graph
marvelG = read_graph('uniq_edges.tsv')

# distance from start (original)
def distance(G, v1, v2):
    distance_from_start = {}
    open_list = [v1]
    distance_from_start[v1] = 0
    while len(open_list) > 0:
        current = open_list[0]
        del open_list[0]
        for neighbor in G[current].keys():
            if neighbor not in distance_from_start:
                distance_from_start[neighbor] = distance_from_start[current] + 1
                if neighbor == v2: return distance_from_start[v2]
                open_list.append(neighbor)
    return False

# path from start (after modification on distance())
def path(G, v1, v2):
    #distance_from_start = {}
    path_from_start = {} # modification
    open_list = [v1]
    #distance_from_start[v1] = 0
    path_from_start[v1] = [v1] # modification
    while len(open_list) > 0:
        current = open_list[0]
        del open_list[0]
        for neighbor in G[current].keys():
            #if neighbor not in distance_from_start:
            if neighbor not in path_from_start: # modification
                #distance_from_start[neighbor] = distance_from_start[current] + 1
                path_from_start[neighbor] = path_from_start[current] 
                                              + [neighbor] # modification
                #if neighbor == v2: return distance_from_start[v2]
                if neighbor == v2: return path_from_start[v2] # modification
                open_list.append(neighbor)
    return False

from_node = "A"
to_node = "ZZZAX"

print distance(marvelG, from_node, to_node)
print path(marvelG, from_node, to_node)

######################### Lesson 19: Centrality #######################

def centrality(G, v):
    distance_from_start = {}
    open_list = [v]
    distance_from_start[v] = 0
    while len(open_list) > 0:
        current = open_list[0]
        del open_list[0]
        for neighbor in G[current].keys():
            if neighbor not in distance_from_start:
                distance_from_start[neighbor] = distance_from_start[current] + 1
                open_list.append(neighbor)
    return float(sum(distance_from_start.values()))/len(distance_from_start)

# UNIT 4 : Magic Trick
#          Computing the best item before the question is asked
#
#           animal        speed weight lifespon brain
#                         (mph)   (kg)  (years) mass (g)
animals = [("dog",          46,   35,    13,  280    ),
           ("elephant",     30, 3500,    50, 6250    ),
           ("frog",         5,     0.5,   8,    3    ),
           ("hippopotamus", 45, 1600,    45,  573    ),
           ("horse",        40,  385,    30,  642    ),
           ("human",        27,   80,    78, 2000    ),
           ("lion",         50,  250,    30,  454    ),
           ("mouse",        8,     0.025, 2,    0.625),
           ("rabbit",       25,    4,    12,   40    ),
           ("shark",        26,  230,    20,   92    ),
           ("sparrow",      16,    0.024, 7,    2    )]

def importance_rank(items, weights):
  names = [animal[0] for animal in animals]
  scores = [sum([a*b for (a, b) in zip(animals[i][1:], weights)]) for i in range(len(animals))]
  results = zip(scores, names)
  results.sort()
  return results

answer = importance_rank(animals, (1, 0.4, 2, 0.1))

for i in range(len(answer)):
  print i, answer[i][1], "(", answer[i][0], ")"


# Tweak the weight values
# Which animal is corresponding to number 3 ?

###################### Code for Lecture 11, Order Statistics:

f = open("yob1995.txt", "r")
maxname = "none"
maxval = 0
max2name = "none"
max2val = 0
for line in f:
    (name,sex,count) = line.rsplit(",")
    count = int(count)
    if sex == "F":
        if count > maxval:
            max2name = maxname
            max2val = maxval
            maxval = count
            maxname = name
        elif count > max2val:
            max2name = name
            max2val = count
print maxname, max2name
print maxval, max2val

########################## Code for Lecture 18, Top K Code:

#
# List of distinct two-digit values.
# Where will 84 be located in the sorted version?
#
import random

L = [31, 45, 91, 51, 66, 82, 28, 33, 11, 89, 27, 36]

def partition(L, v):
    smaller = []
    bigger = []
    for val in L:
        if val < v: smaller += [val]
        if val > v: bigger += [val]
    return (smaller, [v], bigger)

print partition(L, 84)
# >>>[31, 45, 51, 66, 82, 28, 33, 11, 27, 36, 84, 91, 89]

def top_k(L, k):
    v = L[random.randrange(len(L))]
    (left, middle, right) = partition(L, v)
    # middle used below (in place of [v]) for clarity
    if len(left) == k:   return left
    if len(left)+1 == k: return left + middle
    if len(left) > k:    return top_k(left, k)
    return left + middle + top_k(right, k - len(left) - len(middle))

print top_k(L, 5)
# >>> [31, 28, 33, 11, 27]
# list order may vary due to random selection of v

#################################### Code for Lecture 27, Down Heapify

# import random
# L = [random.randrange(90)+10 for i in range(20)]
L = [50, 88, 27, 58, 30, 21, 58, 13, 84, 24, 29, 43, 61, 44 ,65, 74, 76, 30, 82, 43]

#Heap shortcuts
def left(i): return i*2+1
def right(i): return i*2+2
def parent(i): return (i-1)/2
def root(i): return i==0
def leaf(L, i): return right(i) >= len(L) and left(i) >= len(L)
def one_child(L, i): return right(i) == len(L)

# Call this routine if the heap rooted at i satisfies the heap property
# *except* perhaps i to its immediate children
def down_heapify(L, i):
    # If i is a leaf, heap property holds
    if leaf(L, i): return
    # If i has one child...
    if one_child(L, i):
        # check heap property
        if L[i] > L[left(i)]:
            # if it fail, swap, fixing i and its child (a leaf)
            (L[i], L[left(i)]) = (L[left(i)], L[i])
        return
    # if i has two children...
    # check heap property
    if min(L[left(i)], L[right(i)]) >= L[i]: return
    # If it fails, see which child is the smaller
    # and swap i's value into that child
    # Afterwards, recurse into that child, which might violate
    if L[left(i)] < L[right(i)]:
        # Swap into left child
        (L[i], L[left(i)]) = (L[left(i)], L[i])
        down_heapify(L, left(i))
        return
    (L[i], L[right(i)]) = (L[right(i)], L[i])
    down_heapify(L, right(i))
    return