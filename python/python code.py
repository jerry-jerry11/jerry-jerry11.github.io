
def initial_graph() :

    return {

        'A': {'B':3, 'S':7, 'D':4},
        'B': {'A':3, 'S':2, 'H':1, 'D':4},
        'C': {'S':3, 'L':2},
        'D': {'A':4, 'F':5, 'B':4},
        'F': {'D':5, 'H':3},
        'G': {'H':2, 'T':2},
        'H': {'F':3, 'B':1,  'G':2},
        'I': {'J':6, 'K':4,  'L':4},
        'J': {'I':6, 'K':4,  'L':4},
        'K': {'I':4, 'J':4,  'T':5},
        'L': {'I':4, 'J':4,  'C':2},
        'S': {'A':7, 'B':2,  'C':3},
        'T': {'G':2, 'K':5},
            }
 
 
print(initial_graph())
src =input("Enter source node: ")
 
path = {} #Record the cost to each other node
            ##path is NULL
adj_node = {} #Keep track of the path that led us to the destination
 
queue = [] #appends unvisited nodes and to remove the visited nodes
 
graph = initial_graph() #implement the created graph
 
for node in graph: #starting a loop called node to make sure that all nodes are visited
    path[node] = float("inf") #Initially all nodes are assiigned infinity
    adj_node[node] = None
    queue.append(node)

path[src] = 0
 
def alt_func(path, graph, cur_node, i):
    alternate = graph[cur_node][i] + path[cur_node]
    return alternate

def path_func(path, i, alternate):
    path[i] = alternate

def adj_func(adj_node, cur_node, i):
    adj_node[i] = cur_node

while queue:
    # find min distance which wasn't marked as current
    temp_src = queue[0]
    min_cost = path[temp_src] #pick the vertex with minimum distance value and not included in the shortest path.

    ##to update the distance values, iterate through adjacent vertices.
    ##for every adjacent vertex(v):
    for n in range(1, len(queue)):
        ##if (u && u-v) < v then
        ##update distance value of v
        if path[queue[n]] < min_cost: 
            temp_src = queue[n]  
            min_cost = path[temp_src]
    cur_node = temp_src
    queue.remove(cur_node)#Remove the visited node that has been picked up and move to the neighbor with minimum cost
    ##print(cur)
 
    for i in graph[cur_node]:
        alternate = alt_func(path, graph, cur_node, i) ## [i] >> number of nodes in the topology
        if path[i] > alternate:
            path_func(path, i, alternate)
            adj_func(adj_node, cur_node, i)

destination = input('Enter Destination node')
print('The path between ', src, 'to ', destination)
print(destination, end = '<-')
while True:
    destination = adj_node[destination]
    if destination is None:
        print("")
        break
    print(destination, end = '<-')

    