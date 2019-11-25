from data_collection.processes.node_edge_producer import get_all_module_nodes, get_all_edges
from data_collection.processes.author_to_commit import get_author_to_commits_map
author_to_commits_map = get_author_to_commits_map()


def get_module_name_to_commit_dates():
    module_name_to_commit_dates = {}
    for module_node in get_all_module_nodes():
        edges = list(filter(lambda edge: edge.dst.name == module_node.name, get_all_edges()))
        contributor_node_names = list(map(lambda edge: edge.src.name, edges))
        commits = list(map(lambda name: author_to_commits_map[name], contributor_node_names))
        commits_flatten = [item for sublist in commits for item in sublist]
        dates = list(map(lambda commit: commit['date'], commits_flatten))
        module_name_to_commit_dates[module_node.name] = dates
    return module_name_to_commit_dates
