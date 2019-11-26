from data_collection.processes.node_edge_producer import get_all_edges
from data_collection.processes.author_to_commit import get_author_to_commits_map
from common.utils import get_date_quarter_label

author_to_commits_map = get_author_to_commits_map()


def init_date_quarter_labels(module_name):
    final_final_data = {}
    edges = list(filter(lambda edge: edge.dst.name == module_name, get_all_edges()))
    contributor_node_names = list(map(lambda edge: edge.src.name, edges))
    for author in author_to_commits_map.keys():
        if author in contributor_node_names:
            commits = author_to_commits_map[author]
            for commit in commits:
                date = commit['date']
                quarter_label = get_date_quarter_label(date)
                try:
                    final_final_data[quarter_label]
                except:
                    final_final_data[quarter_label] = {}
    return final_final_data


def get_contributors_to_lines_changed_given_module(module_name, given_quarter_label):
    edges = list(filter(lambda edge: edge.dst.name == module_name, get_all_edges()))
    contributor_node_names = list(map(lambda edge: edge.src.name, edges))
    final_data = {}
    for author in author_to_commits_map.keys():
        if author in contributor_node_names:
            commits = author_to_commits_map[author]
            all_commits_addition_sum = 0
            all_commits_deletion_sum = 0
            for commit in commits:
                date = commit['date']
                quarter_label = get_date_quarter_label(date)
                if quarter_label == given_quarter_label:
                    files_changed_in_this_module = list(filter(lambda file: module_name in file['filepath'] , commit['files']))
                    all_commits_addition_sum += sum(map(lambda file: file['additions'], files_changed_in_this_module))
                    all_commits_deletion_sum += sum(map(lambda file: file['deletions'], files_changed_in_this_module))
            final_data[author] = {
                'additions': all_commits_addition_sum,
                'deletions': all_commits_deletion_sum
            }
    return final_data


def get_quarter_label_to_vis3_data(module_name):
    quarter_label_to_vis3_data = init_date_quarter_labels(module_name)
    for quarter_label in quarter_label_to_vis3_data.keys():
        quarter_label_to_vis3_data[quarter_label] = get_contributors_to_lines_changed_given_module(module_name, quarter_label)
    return quarter_label_to_vis3_data
