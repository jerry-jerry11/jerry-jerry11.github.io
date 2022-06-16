from PyQt5.QtWidgets import *
from PyQt5.Qt import *
import sys
class Application(QMainWindow):
    def __init__(self):
        super(Application, self).__init__()
        #We create a dictionary to represent the graph
        self.graph = {
            'a': {'b': 3, 'd': 4, 's': 7},
            'b': {'a': 3, 'd': 4, 'h': 1, 's': 2},
            'c': {'s': 3, 'l': 2},
            'd': {'a': 4, 'b': 4, 'f': 5},
            'f': {'d': 5, 'h': 3},
            'g': {'h': 2, 't': 2},
            'h': {'b': 1, 'f': 3, 'g': 2},
            'i': {'k': 4, 'j': 6, 'l': 4},
            'j': {'i': 6, 'k': 4, 'l': 4},
            'k': {'j': 4, 'i': 4, 't': 5},
            'l': {'c': 2, 'i': 4, 'j': 4},
            's': {'a': 7, 'b': 2, 'c': 3},
            't': {'g': 2, 'k': 5},
        }
        #The following piece of code sets the display window when executing the code
        self.setFixedSize(900, 600)
        self.field = QLineEdit("D-J", self)
        self.field.setGeometry(300, 60, 300, 40)
        self.field.setAlignment(Qt.AlignCenter)
        self.field.setStyleSheet("Font-size:20px")
        self.field.returnPressed.connect(self.onClick)
        self.lbl = QLabel(" ", self)
        self.lbl.setGeometry(0, 530, 900, 40)
        self.lbl.setAlignment(Qt.AlignCenter)
        self.lbl.setStyleSheet("Font-size:20px;color:orange")
        self.background = QLabel(self)
        self.background.setGeometry(150, 110, 800, 400)
        self.background.setPixmap(QPixmap("Topology.PNG"))
        self.show()
    def onClick(self):
        s, d = str(self.field.text()).split("-")
        self.dijkstra_method(str(s).lower(), str(d).lower())
    def dijkstra_method(self, source, destination): #Main function, Passed parameter self,source and destination 
        shortDistance = {}  # To store the record cost to reach other node
        track_precedessor = {}  # Storing the path that will be used to reach the destination
        unseen_nodes = self.graph  # To iterate through the entire graph
        infinity = 9999999  # Assigning the variable to all nodes
        track_path = []  # Tracing the journey back to the source node
        for node in unseen_nodes:  # initialising state
            shortDistance[node] = infinity  # Assigning all nodes with a large number
        shortDistance[source] = 0  # On the initial working node we assign 0
        while unseen_nodes:
            minDistance_node = None  # Initially there's not going to be a minimun distance
            for node in unseen_nodes:  # this graph has n nodes
                if minDistance_node is None:
                    minDistance_node = node
                elif shortDistance[node] < shortDistance[minDistance_node]:
                    minDistance_node = node
            path_options = self.graph[minDistance_node].items()  # Each when we figure out the short distance and the node, we want to know the possible next links
            for mini_node, weight in path_options:
                if weight + shortDistance[minDistance_node] < shortDistance[mini_node]:
                    shortDistance[mini_node] = weight + shortDistance[minDistance_node]
                    track_precedessor[mini_node] = minDistance_node
            unseen_nodes.pop(minDistance_node)  # Flag the node visited
        current_node = destination
        while current_node != source:  # applying the exception if the destination node is not reachable
            try:
                track_path.insert(0, current_node)
                current_node = track_precedessor[current_node]  # This will help us to go back
            except KeyError:
                self.lbl.setText("Invalid path")  # Error message for if the destination node is not reachable
                break
        track_path.insert(0, source)
        tracks = []
        for t in track_path:
            t = str(t).upper()
            tracks.append(t)
        track = " --- ".join(tracks)
        if shortDistance[destination] != infinity:  # This line to check if we were able to reach the destination
            self.lbl.setText(track + " = " + str(shortDistance[destination]))  # Output the Results
app = QApplication(sys.argv)
a = Application()
app.exec_()

