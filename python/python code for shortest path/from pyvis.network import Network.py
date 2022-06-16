from pyvis.network import Network
# All networks must be instantiated as a Network class instance
net = Network()
#Next, add nodes to the network
net.add_node(1, label="Sreeni") # node id = 1 and label = Sreeni
net.add_node(2) # node id and label = 2. No specific label assigned.

#The ID parameter must be unique
#To show the network, use net.show. This saves a html file at the specified path with the specified name. 
net.show('nodes.html')
# To display this html file in order to interact with the network
from IPython.core.display import display, HTML
display(HTML("nodes.html"))
#You will see two unconnected nodes.
#Instead of single nodes at a time, we can add list of nodes.
from IPython.core.display import display, HTML
net1 = Network()
nodes = ["a", "b", "c", "d"]
labels = ["Sreeni", "Mike", "Imran", "Syed"]
net1.add_nodes(nodes, label=labels) 
net1.show('nodes1.html')
display(HTML("nodes1.html"))
#We can add color to our nodes to make them look pretty
from IPython.core.display import display, HTML
net2 = Network()
nodes = ["a", "b", "c", "d"]
labels = ["Sreeni", "Mike", "Imran", "Syed"]
colors=['#FF0000', '#00CC00', '#0000CC', '#FFCC00']
net2.add_nodes(nodes, label=labels, color=colors) 
net2.show('nodes2.html')
display(HTML("nodes2.html"))
#Now, let us connect these nodes using edges. 
net2.add_edges([("a","b"), ("a", "d")])
net2.show('edges.html')
display(HTML("edges.html"))
#What if my friendship with Syed is stronger than with Mike? We can add weight to reflect that.
net3 = Network()
nodes = ["a", "b", "c", "d"]
labels = ["Sreeni", "Mike", "Imran", "Syed"]
colors=['#FF0000', '#00CC00', '#0000CC', '#FFCC00']
net3.add_nodes(nodes, label=labels, color=colors) 

net3.add_edges([("a","b", 1), ("a", "d", 5)]) #Friendship with Syed is 5 times compared to Mike. 
net3.show('edges2.html')
display(HTML("edges2.html"))
#The node distance and spring length can be changed using the repulsion method. 
net3.repulsion(node_distance=90, spring_length=200)
net3.show('edges3.html')
display(HTML("edges3.html"))

import pandas as pd
import numpy as np
my_friends = [
    ("Sreeni", "Mike"),
    ("Sreeni", "Imran"),
    ("Sreeni", "Mustafa"),
    ("Sreeni", "Syed"),
    ("Sreeni", "Satya"),
    ("Sreeni", "Vamsi"),
    ("Imran", "Mustafa"),
    ("Imran", "Mike"),
    ("Mustafa", "Satya"),
    ("Mustafa", "Vamsi"),
    ("Syed", "Mike"),
    ("Syed", "Satya")
]
friends = pd.DataFrame(my_friends, columns=["friend1", "friend2"])
#Let us get all the names as a list. 
#The easiest way to achieve this is by getting all unique names from each column 
#and finding the union of both. This means we need to capture the data as 'set' and not a list or array or tuple. 

#Crash course on sets in python
a = set([1,1,1,2,3,4,4,5,5,5])
b = set([4,4, 5, 6, 7, 7, 8])
print(a)
print(b)
print("Now capturing the union of both sets")
u = a.union(b)
print(u)
{1, 2, 3, 4, 5}
{4, 5, 6, 7, 8}
{1, 2, 3, 4, 5, 6, 7, 8}
#Now, let us get the unique list of our friends from our dataframe
people = list(set(friends.friend1).union(set(friends.friend2))) 
print(people)
['Syed', 'Mike', 'Imran', 'Vamsi', 'Satya', 'Sreeni', 'Mustafa']
#Define the network and add friends to the nodes. 
from pyvis.network import Network

friends_net = Network(notebook=True)
friends_net.add_nodes(people)
my_friends_list = friends.values.tolist()
my_friends_list
[['Sreeni', 'Mike'],
 ['Sreeni', 'Imran'],
 ['Sreeni', 'Mustafa'],
 ['Sreeni', 'Syed'],
 ['Sreeni', 'Satya'],
 ['Sreeni', 'Vamsi'],
 ['Imran', 'Mustafa'],
 ['Imran', 'Mike'],
 ['Mustafa', 'Satya'],
 ['Mustafa', 'Vamsi'],
 ['Syed', 'Mike'],
 ['Syed', 'Satya']]
#Now, let us add edges and viusualize our network 
friends_net.add_edges(my_friends_list)
friends_net.show("my_friends_map.html")

from IPython.core.display import display, HTML
display(HTML("my_friends_map.html"))
