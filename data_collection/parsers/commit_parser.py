import json
import os

data_collection_dir_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def get_commit_essentials(commit_json):
    return {
        'sha': commit_json.get('sha'),
        'author_login': commit_json['author']['login'],
        'date': commit_json['commit']['author']['date']
    }


file_path = os.path.join(data_collection_dir_path, 'data/commits.json')
all_commits = json.load(open(file_path))
all_commits_reduced = []
commits_reduced_file_path = os.path.join(data_collection_dir_path,'data/commits_reduced.json')
for commit_json in all_commits:
    try:
        all_commits_reduced.append(get_commit_essentials(commit_json))
    except Exception as e:
        print(json.dumps(commit_json))

with open(commits_reduced_file_path, 'w') as f:
    f.write(json.dumps(all_commits_reduced))
