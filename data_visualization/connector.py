from data_visualization.visualizer import Bipartite


def plot(contributorPerFileObject):
    try:
        vis = Bipartite()
        for contributor, modules in contributorPerFileObject:
            vis.insert_contributor_node(contributor)
            for module in modules:
                i = module['rate']
                name = module['name']
                vis.insert_module_node(name)
                while i > 0:
                    vis.insert_edge((name, chr(contributor)))
                    i=i-1
    except TypeError as e:
        print(e)
