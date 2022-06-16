from decimal import Decimal

class Node:
    def __init__(self, label):
        self.label = label

class Edge:
    def __init__(self, to_node, length):
        self.to_node = to_node
        self.length = length


class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = dict()

    def add_node(self, node):
        self.nodes.add(node)

    def add_edge(self, from_node, to_node, length):
        edge = Edge(to_node, length)
        if from_node.label in self.edges:
            from_node_edges = self.edges[from_node.label]
        else:
            self.edges[from_node.label] = dict()
            from_node_edges = self.edges[from_node.label]
        from_node_edges[to_node.label] = edge


def min_dist(q, dist):
    """
    Returns the node with the smallest distance in q.
    Implemented to keep the main algorithm clean.
    """
    min_node = None
    for node in q:
        if min_node == None:
            min_node = node
        elif dist[node] < dist[min_node]:
            min_node = node

    return min_node

INFINITY = Decimal('Infinity')

def dijkstra(graph, source):
    q = set()
    dist = {}
    prev = {}

    for v in graph.nodes:       # initialization
        dist[v] = INFINITY      # unknown distance from source to v
        prev[v] = INFINITY      # previous node in optimal path from source
        q.add(v)                # all nodes initially in q (unvisited nodes)

    # distance from source to source
    dist[source] = 0

    while q:
        # node with the least distance selected first
        u = min_dist(q, dist)

        q.remove(u)

        if u.label in graph.edges:
            for _, v in graph.edges[u.label].items():
                alt = dist[u] + v.length
                if alt < dist[v.to_node]:
                    # a shorter path to v has been found
                    dist[v.to_node] = alt
                    prev[v.to_node] = u

    return dist, prev


def to_array(prev, from_node):
    """Creates an ordered list of labels as a route."""
    previous_node = prev[from_node]
    route = [from_node.label]

    #bubble sorting
    while previous_node != INFINITY:
        route.append(previous_node.label)
        temp = previous_node
        previous_node = prev[temp]

    route.reverse()
    return route


graph = Graph()
node_a = Node("A")
graph.add_node(node_a)
node_b = Node("B")
graph.add_node(node_b)
node_c = Node("C")
graph.add_node(node_c)
node_d = Node("D")
graph.add_node(node_d)
node_s = Node("S")
graph.add_node(node_s)
node_f = Node("F")
graph.add_node(node_f)
node_g = Node("G")
graph.add_node(node_g)
node_h = Node("H")
graph.add_node(node_h)
node_i = Node("I")
graph.add_node(node_i)
node_j = Node("J")
graph.add_node(node_j)
node_k = Node("K")
graph.add_node(node_k)
node_l = Node("L")
graph.add_node(node_l)
node_t = Node("T")
graph.add_node(node_t)

graph.add_edge(node_a, node_b, 3)
graph.add_edge(node_a, node_d, 4)
graph.add_edge(node_a, node_s, 7)
graph.add_edge(node_b, node_a, 3)
graph.add_edge(node_b, node_d, 4)
graph.add_edge(node_b, node_s, 2)
graph.add_edge(node_b, node_h, 1)
graph.add_edge(node_c, node_l, 2)
graph.add_edge(node_c, node_s, 3)
graph.add_edge(node_d, node_a, 4)
graph.add_edge(node_d, node_b, 4)
graph.add_edge(node_d, node_f, 5)
graph.add_edge(node_f, node_d, 5)
graph.add_edge(node_f, node_h, 3)
graph.add_edge(node_h, node_b, 1)
graph.add_edge(node_h, node_g, 3)
graph.add_edge(node_h, node_f, 3)
graph.add_edge(node_g, node_h, 2)
graph.add_edge(node_g, node_t, 2)
graph.add_edge(node_i, node_j, 6)
graph.add_edge(node_i, node_l, 4)
graph.add_edge(node_i, node_k, 4)
graph.add_edge(node_j, node_i, 6)
graph.add_edge(node_j, node_k, 4)
graph.add_edge(node_j, node_l, 4)
graph.add_edge(node_k, node_i, 4)
graph.add_edge(node_k, node_j, 4)
graph.add_edge(node_k, node_t, 5)
graph.add_edge(node_l, node_c, 2)
graph.add_edge(node_l, node_j, 4)
graph.add_edge(node_l, node_i, 4)
graph.add_edge(node_t, node_g, 2)
graph.add_edge(node_t, node_k, 4)
graph.add_edge(node_s, node_c, 3)
graph.add_edge(node_s, node_b, 2)
graph.add_edge(node_s, node_a, 7)

node_d=input("enter source node: ")
dist=input("Enter destination node: ")
dist, prev = dijkstra(graph,node_d)

print("The quickest path from {} to {} is [{}] with a distance of {}".format(
    node_d.label,
    node_j.label,
    " -> ".join(to_array(prev, node_j)),
    str(dist[node_j])
    )
)