from data_visualization.visualizer import Bipartite


def plot(module_nodes, contributor_nodes, edges):
    try:
        vis = Bipartite()
        for contributor_node in contributor_nodes[:20]:
            vis.insert_contributor_node(contributor_node.name)

        for module_node in module_nodes[:5]:
            vis.insert_module_node(module_node.name)

        # for edge in edges:
        #     i = edge.weight
        #
        #     while i > 0:
        #         i = i-1
        #         vis.insert_edge((edge.dst.name, chr(edge.src.name)))

        vis.show()
    except TypeError as e:
        print('error: ' + str(e))