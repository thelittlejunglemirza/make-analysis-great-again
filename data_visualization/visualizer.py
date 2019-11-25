import networkx as nx
import matplotlib.pyplot as plt

# CONSTANTS
change_color_to_blue_limit = 2.0
change_color_to_green_limit = 5.0
change_color_to_red_limit = 7.0

class Bipartite:
    def __init__(self):
        self.B = nx.Graph()
        self.__edges = []
        self.__edge_widths = []
        self.__edge_colors = []
        self.__nodes_type_1 = []
        self.__nodes_type_2 = []
        self.__node_size_type_1 = []
        self.__node_size_type_2 = []
        self.__node_color_type_1 = []
        self.__node_color_type_2 = []
        self.__positions = {}

    # each edge should be of the from:
    # (Module, Contributor)
    # Module and Contributor must be exact value
    # for what is passed to nodes array
    # HANDLES EDGE WEIGHT AND COLOR
    def insert_edge(self, edge):
        if isinstance(edge, tuple):
            if edge in self.__edges:
                # if edge already exists add to its weight
                idx = self.__edges.index(edge)
                if self.__edge_widths[idx] < 8:
                    self.__edge_widths[idx] += 1.0
                # change the color if weight too big
                if self.__edge_widths[idx] >= change_color_to_red_limit:
                    self.__edge_colors[idx] = 'r'
                elif self.__edge_widths[idx] >= change_color_to_green_limit:
                    self.__edge_colors[idx] = 'g'
                elif self.__edge_widths[idx] >= change_color_to_blue_limit:
                    self.__edge_colors[idx] = 'b'
            else:
                self.__edges.append(edge)
                self.__edge_widths.append(1.0)
                self.__edge_colors.append('black')
        else:
            raise TypeError('cannot insert edge: edge is not a tuple')

    # add type one node
    def insert_module_node(self, node):
        self.__nodes_type_1.append(node)
        self.__node_size_type_1.append(200)
        self.__node_color_type_1.append('r')

    # add type two node
    def insert_contributor_node(self, node):
        self.__nodes_type_2.append(node)
        self.__node_size_type_2.append(50)
        self.__node_color_type_2.append('y')

    # generate the positions for nodes
    # making sure the order is consistent
    def __update_positions(self):
        self.__positions = {}
        # Separate by group
        left = {n for n, d in self.B.nodes(data=True) if d['bipartite'] == 0}
        right = sorted(set(self.B) - left)
        # need to sort after right because of set deduction above
        left = sorted(left)
        # Update position for node from each group
        new_arr = []
        margin_left = 0
        for index, node in enumerate(left):
            # self.__positions.update((node, (1, index + margin_left)))
            # self.__positions.update((node, (1, index + margin_left)))
            new_arr.append((node, (1, index + margin_left)))
            margin_left += 200000

        margin_right = 0
        for index, node in enumerate(right):
            # self.__positions.update((node, (2, index + margin_right)))
            # self.__positions.update((node, (1, index + margin_right)))
            new_arr.append((node, (2, index + margin_right)))
            margin_right += 10000
        self.__positions.update(new_arr)

    # actually load the data to graph
    def update_graph(self):
        # add all the nodes
        self.B.add_nodes_from(self.__nodes_type_1, bipartite=0)
        self.B.add_nodes_from(self.__nodes_type_2, bipartite=1)
        print(self.B.nodes)
        # add all the edges
        self.B.add_edges_from(self.__edges)
        self.__update_positions()

    # re-arrange nodes to left and right
    # make it look nice and organized
    # and draw
    def draw(self):
        # optional parameters:
        #   node_size  (default=3000) , could be an array for each node
        #   node_color (default='r') , could be an array for each node
        #   width      (size of edges default=1.0) , could be an array for each node
        #   edge_cmap  (Matplotlib colormap, optional (default=None))
        nx.draw_networkx(self.B,
                         pos=self.__positions,
                         with_labels=False,
                         node_size=self.__node_size_type_1+self.__node_size_type_2,
                         node_color=self.__node_color_type_1+self.__node_color_type_2,
                         width=self.__edge_widths,
                         edge_color=self.__edge_colors,
                         font_size=8)

    def show(self):
        self.update_graph()
        self.draw()
        plt.show()


# # PLAYING WITH GRAPH MODULE
# vis = Bipartite()
# for i in range(1, 6):
#     vis.insert_module_node(i)
#
# try:
#     i = 1
#     for code in range(ord('a'), ord('e') + 1):
#         vis.insert_contributor_node(chr(code))
#         vis.insert_edge((i, chr(code)))
#         for j in range(i-1):
#             vis.insert_edge((i, chr(code)))
#         i += 1
# except TypeError as e:
#     print(e)
