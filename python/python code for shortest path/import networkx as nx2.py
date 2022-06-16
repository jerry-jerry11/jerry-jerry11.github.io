import networkx as nx
 
G = nx.Graph()
 
G.add_edges_from([('A', 'B'), ('A', 'K'), ('B', 'K'), ('A', 'C'),
                  ('B', 'C'), ('C', 'F'), ('F', 'G'), ('C', 'E'),
                  ('E', 'F'), ('E', 'D'), ('E', 'H'), ('I', 'J')])
 
nx.draw_networkx(G, with_labels = True, node_color ='green')
 
# returns True or False whether Graph is connected
print(nx.is_connected(G))
 
# returns number of different connected components
print(nx.number_connected_components(G))
 
# returns list of nodes in different connected components
print(list(nx.connected_components(G)))
 
# returns list of nodes of component containing given node
print(nx.node_connected_component(G, 'I'))
 
# returns number of nodes to be removed
# so that Graph becomes disconnected
print(nx.node_connectivity(G))
 
# returns number of edges to be removed
# so that Graph becomes disconnected
print(nx.edge_connectivity(G))