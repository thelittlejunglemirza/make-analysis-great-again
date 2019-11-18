import json


class GitHubCommit:
    def __init__(self, commit, client):
        print(commit['sha'])
        print(commit['author']['login'])
        print(commit['commit']['author']['date'])
        self.sha = commit['sha']
        self.author_login = commit['author']['login']
        self.date = commit['commit']['author']['date']
        self.client = client

    def get_files_changed(self):
        files = json.loads(json.dumps(self.client.get_commit_info(self.sha)))['files']
        filenames = []
        for f in files:
            filenames.append(f['filename'])
        return filenames


class GitHubCollaborator:
    def __init__(self, commit):
        print(commit['login'])
        self.login = commit['login']


class GitHubRepoInfo:
    pass


class RepositoryFile:
    pass

