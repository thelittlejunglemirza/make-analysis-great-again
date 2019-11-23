from data_collection.processes.author_to_commit import get_author_to_commits_map
from data_visualization.structures import Node, Edge
from data_collection.helpers import FileHierarchy, sort_dict_per_value
edges = []
nodes = []


author_to_commit = get_author_to_commits_map()


def get_all_file_paths():
    all_file_paths = []
    for commits in author_to_commit.values():
        for commit in commits:
            file_paths = list(map(lambda file: file['filepath'], commit['files']))
            for file_path in file_paths:
                if file_path not in all_file_paths:
                    all_file_paths.append(file_path)
    return all_file_paths


def get_all_module_nodes():
    pass
        # print(commits)
    # map(lambda v: list(map(lambda v2: filepaths.extend(v2['files']), v)), author_to_commit.values())
    # return filepaths


def get_all_contributor_nodes():
    pass


def get_all_nodes():
    return get_all_module_nodes() + get_all_contributor_nodes()


def get_all_edges():
    pass


def get_modules():
    file_paths = get_all_file_paths()
    fh = FileHierarchy(file_paths)
    mapping = fh.get_components_to_num_files_map()
    # module: folders with most number of files in it
    print(sort_dict_per_value(mapping))


get_modules()
