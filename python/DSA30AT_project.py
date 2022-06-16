## Consists of the vertex(source), adjacent vertices(neighbors) and the weight of edge(distance between two nodes)
topology_graph = {'A': {'B':3, 'S':7, 'D':4},
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
        'T': {'G':2, 'K':5},}
 
def topology(topology_graph,src,goal):
    min_distance = {}
    predecessor = {} 
    unvisited = topology_graph ##vertices in the graph that are not yet included in the shortest path set
    infinity = 99999
    path = [] ## The Path is initially empty
    for node in unvisited:
        min_distance[node] = infinity ##all the distance values(v) are initialed to infinity.
    min_distance[src] = 0 ##distance value of 0 is assigned to the source vertex(node) that is picked first.
 
    while unvisited: ## while the vertices are not included...
        minNode = None ## the adjacent vertice with the minimum distance is set to NULL.

        ##to update the distance values, iterate through adjacent vertices.
        ##for every adjacent vertex(v):
        for node in unvisited: 

            ##if (u && u-v) < v then
            ##update distance value of v
            if minNode is None:
                minNode = node
            elif min_distance[node] < min_distance[minNode]:
                minNode = node
 
        for adj_vert, cost in topology_graph[minNode].items():
            if cost + min_distance[minNode] < min_distance[adj_vert]:
                min_distance[adj_vert] = cost + min_distance[minNode]
                predecessor[adj_vert] = minNode
        unvisited.pop(minNode) ##Returns the recently visited vertice of the parent node and iterate through the adjacent vertices.
    ##Goal is the destination
    currentNode = goal 
    while currentNode != src:##while the node that was updated is not the source node
        try:
            path.insert(0,currentNode)##inserting the updated node to the path.
            currentNode = predecessor[currentNode]##predecessor node in the left sub-tree with the maximum updated distance.
        except KeyError:
            print('Path invalid')
            break
    def src_funt(src, path):
        path.insert(0,src) ##the vertex is then inserted in the path
    src_funt(src, path)## call the function

    if min_distance[goal] != infinity: ##if the node with minimum distance is not marked as infinite
        ##print/display the shortest path and its overall cost.
        print('Shortest distance is ' + str(min_distance[goal]))
        print('And the path is ' + str(path))
 
 
topology(topology_graph, src=input("Enter source: "), goal=input("Enter dest: ")) ## call the function that was defined 