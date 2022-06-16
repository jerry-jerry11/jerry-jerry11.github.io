from re import A
import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_edge('A', 'B', weight = 3)
G.add_edge('A', 'D', weight = 4)
G.add_edge('A', 'S', weight = 7)
G.add_edge('B', 'D', weight = 4)
G.add_edge('B', 'S', weight = 2)
G.add_edge('B', 'H', weight = 1)
G.add_edge('C', 'S', weight = 3)
G.add_edge('D', 'F', weight = 5)
G.add_edge('F', 'H', weight = 3)
G.add_edge('H', 'G', weight = 2)
G.add_edge('G', 'T', weight = 2)
G.add_edge('C', 'L', weight = 2)
G.add_edge('L', 'I', weight = 4)
G.add_edge('L', 'J', weight = 4)
G.add_edge('I', 'J', weight = 6)
G.add_edge('I', 'K', weight = 4)
G.add_edge('J', 'K', weight = 4)
G.add_edge('T', 'K', weight = 5)


# explicitly set positions
pos = {'A': (-3.4, 0.6), 'B': (-0.4, 0.5), 'S': (-1.1, 0.8), 'D': (-3.4, 0.255), 'C': (2.0, 0.8), 'F': (-2.6, -0.1), 'H': (-0.5, 0.1), 'G': (1.1, -0.0), 'T': (2.7, -0.1), 
      'L': (3.7, 0.7), 'I': (3.1, 0.4), 'J': (4.8, 0.4), 'K': (3.8, 0.1)}

options = {
    "font_size": 36,
    "node_size": 3000,
    "node_color": "blue",
    "edgecolors": "black",
  
    "linewidths": 5,
    "width": 5,
}
nx.draw_networkx(G, pos, **options)
plt.title("GRAPH TOPOLOGY")


# Set margins for the axes so that nodes aren't clipped
ax = plt.gca()
ax.margins(0.20)
plt.axis("off")
plt.show()