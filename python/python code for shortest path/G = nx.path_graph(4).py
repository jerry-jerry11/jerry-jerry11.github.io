G = nx.path_graph(4)
sequence = (d for n, d in G.degree())
nx.is_graphical(sequence)
True