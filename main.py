from data_collection.github_client import GitHubClient

username = 'django'
repository = 'django'
client = GitHubClient(username, repository)

client.get_collaborators()
