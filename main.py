from data_collection.github_client import GitHubClient
import json

username = 'django'
repository = 'django'
client = GitHubClient(username, repository)

client.get_commits(1)


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
