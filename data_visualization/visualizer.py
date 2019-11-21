import networkx as nx
from data_collection.models import GitHubCommit, GitHubCollaborator
from data_collection.github_client import GitHubClient
import json
import requests
from networkx.algorithms import bipartite


class Visualization:
    def __init__(self):
        self.B = nx.Graph()

    def insert_edges(self, edges):
        for edge in edges:
            self.B.add_edge(edge.collaborator, edge.module)

    def insert_nodes(self, nodes, bit):
        self.B.add_nodes_from(nodes, bipartite=bit)


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


commits = []
collaborators = []
modules = []
for i in range(5):
    collaborators.append(DummyCollaborator(("login" + str(i))))
for i in range(5):
    modules.append(DummyModule(("module" + str(i))))
for i in range(5):
    commits.append(DummyCommit(collaborators[i], modules[i], i))
vis = Visualization()
vis.insert_nodes(collaborators, 1)
vis.insert_nodes(modules, 0)
vis.insert_edges(commits)
nx.draw(vis.B, with_labels=True, font_weight='bold')
