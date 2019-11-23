import networkx as nx
import matplotlib.pyplot as plt
from data_collection.models import GitHubCommit, GitHubCollaborator
from data_collection.github_client import GitHubClient
import json
import requests
from networkx.algorithms import bipartite


class Bipartite:
    def __init__(self):
        self.B = nx.Graph()
        self.__edges = []
        self.__edge_widths = []
        self.__nodes_type_1 = []
        self.__nodes_type_2 = []
        self.G = None

    # each edge should be of the from:
    # (Module, Contributor)
    # Module and Contributor must be exact value
    # for what is passed to nodes array
    def insert_edge(self, edge):
        if isinstance(edge, tuple):
            if edge in self.__edges:
                # if edge already exists add to its weight
                idx = self.__edges.index(edge)
                self.__edge_widths[idx] += 1.0
            else:
                self.__edges.append(edge)
                self.__edge_widths.append(1.0)
        else:
            raise TypeError('cannot insert edge: edge is not a tuple')

    # add type one node
    def insert_module_node(self, node):
        self.__nodes_type_1.append(node)

    # add type two node
    def insert_contributor_node(self, node):
        self.__nodes_type_2.append(node)

    # actually load the data to graph
    def update_graph(self):
        # add all the nodes
        self.B.add_nodes_from(self.__nodes_type_1, bipartite=0)
        self.B.add_nodes_from(self.__nodes_type_2, bipartite=1)
        # add all the edges
        self.B.add_edges_from(self.__edges)

    # re-arrange nodes to left and right
    # make it look nice and organized
    # and draw
    def draw(self):
        # optional parameters:
        #   node_size  (default=3000)
        #   node_color (default='r')
        #   width      (size of edges default=1.0)
        #   edge_cmap  (Matplotlib colormap, optional (default=None))
        nx.draw_networkx(vis.B,
                         pos=nx.drawing.layout.bipartite_layout(self.B, self.__nodes_type_1),
                         with_labels=True,
                         width=self.__edge_widths,
                         font_weight='bold')


# PLAYING WITH GRAPH MODULE
vis = Bipartite()
for i in range(1, 6):
    vis.insert_module_node(i)

try:
    i = 1
    for code in range(ord('a'), ord('e') + 1):
        vis.insert_contributor_node(chr(code))
        vis.insert_edge((i, chr(code)))
        for j in range(i):
            vis.insert_edge((i, chr(code)))
        i += 1
except TypeError as e:
    print(e)

vis.update_graph()
vis.draw()
plt.show()

# print('done')
