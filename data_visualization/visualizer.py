import networkx as nx
import matplotlib.pyplot as plt
from data_collection.models import GitHubCommit, GitHubCollaborator
from data_collection.github_client import GitHubClient
import json
import requests
from networkx.algorithms import bipartite


class Visualization:
    def __init__(self):
        self.B = nx.Graph()
        self.__edges = []
        self.__nodes_type_1 = []
        self.__nodes_type_2 = []
        self.G = None

    # each edge should be of the from:
    # (Module, Contributor)
    # Module and Contributor must be exact value
    # for what is passed to nodes array
    def insert_edge(self, edge):
        if isinstance(edge, tuple):
            self.__edges.append(edge)
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

    # re-arrange nodes to top and bottom
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
                         arrows=True,
                         with_labels=True,
                         width=5.0,
                         font_weight='bold')


class DummyCommit:
    def __init__(self, collaborator, module, change):
        self.collaborator = collaborator
        self.module = module
        self.change = change


class DummyCollaborator:
    def __init__(self, login):
        self.login = login


class DummyModule:
    def __init__(self, name):
        self.name = name


# G = nx.bipartite.gnmk_random_graph(3, 5, 10, seed=123)
# top = nx.bipartite.sets(G)[0]
# pos = nx.bipartite_layout(G, top)

# PLAYING WITH GRAPH MODULE
vis = Visualization()
for i in range(1, 6):
    vis.insert_module_node(i)

try:
    i = 1
    for code in range(ord('a'), ord('e') + 1):
        vis.insert_contributor_node(chr(code))
        vis.insert_edge((i, chr(code)))
        i += 1
except TypeError as e:
    print(e)

vis.update_graph()
vis.draw()
plt.show()

# vis = Visualization()


# commits = []
# collaborators = []
# modules = []
# for i in range(5):
#     collaborators.append(DummyCollaborator(("login" + str(i))))
# for i in range(5):
#     modules.append(DummyModule(("module" + str(i))))
# for i in range(5):
#     commits.append(DummyCommit(collaborators[i], modules[i], i))
# vis = Visualization()
# vis.insert_nodes(collaborators, 1)
# vis.insert_nodes(modules, 0)
# vis.insert_edges(commits)
# nx.draw(vis.B, with_labels=True, font_weight='bold')
# plt.show()
# print('done')
