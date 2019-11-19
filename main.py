from data_collection.github_client import GitHubClient
from data_collection.models import GitHubCommit
import json

# username = 'django'
# repository = 'django'
# client = GitHubClient(username, repository)
#
# commits = client.get_commits(1)
#
# commit = GitHubCommit(json.loads(json.dumps(commits))[0], client)
# print(commit.get_files_changed())

sha_author_dict = {}

try:
    # read file
    with open('data_collection/data/commits_reduced.json', 'r') as my_file:
        data = my_file.read()

    # parse reduced file
    obj = json.loads(data)
    for o in obj:
        sha_author_dict[o['sha']] = o['author_login']

except Exception as e:
    print('caught error in reading reduced data: ' + str(e))

author_to_commit = {}
try:
    with open('data_collection/data/commits_detailed.json', 'r') as my_file:
        data = my_file.read()
    # parsing detailed file
    obj = json.loads(data)
    for o in obj:
        temp_obj = {'sha': o['sha'], 'date': o['commit']['author']['date'], 'files': []}
        for file in o['files']:
            temp_obj['files'].append(file['filename'])
        if o['author']['login'] in author_to_commit:
            author_to_commit[o['author']['login']].append(temp_obj)
        else:
            author_to_commit[o['author']['login']] = []
            author_to_commit[o['author']['login']].append(temp_obj)
except Exception as e:
    print('caught error in reading detailed data: ' + str(e))

print(len(author_to_commit.keys()))

# date_to_commits = []
# for k in author_to_commit.keys():
#     for c in  author_to_commit[k]:

print(author_to_commit)

# json.dumps()
# commit_list = []

# recent_result = []

# page = 1
# while True:
#     print(page)
#     recent_result = client.get_commits(page)
#     page = page + 1
#     if len(recent_result) == 0:
#         break
#     commit_list.extend(recent_result)
#
#
# print(commit_list)
