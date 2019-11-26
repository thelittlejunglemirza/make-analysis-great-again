from data_collection.processes.node_edge_producer import get_all_edges
from data_collection.processes.author_to_commit import get_author_to_commits_map
author_to_commits_map = get_author_to_commits_map()


def get_contributors_to_lines_changed_given_module(module_name):
    edges = list(filter(lambda edge: edge.dst.name == module_name, get_all_edges()))
    contributor_node_names = list(map(lambda edge: edge.src.name, edges))
    final_data = {}
    for author in author_to_commits_map.keys():
        if author in contributor_node_names:
            commits = author_to_commits_map[author]
            all_commits_addition_sum = 0
            all_commits_deletion_sum = 0
            for commit in commits:
                files_changed_in_this_module = list(filter(lambda file: module_name in file['filepath'] , commit['files']))
                all_commits_addition_sum += sum(map(lambda file: file['additions'], files_changed_in_this_module))
                all_commits_deletion_sum += sum(map(lambda file: file['deletions'], files_changed_in_this_module))
            final_data[author] = {
                'additions': all_commits_addition_sum,
                'deletions': all_commits_deletion_sum
            }
    return final_data

# get_contributors_to_lines_changed_given_module('django/utils')
