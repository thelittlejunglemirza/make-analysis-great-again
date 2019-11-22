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

# date_to_commits = []
# for k in author_to_commit.keys():
#     for c in  author_to_commit[k]:

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
