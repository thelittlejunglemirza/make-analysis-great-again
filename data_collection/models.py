class GitHubCommit:
    def __init__(self, JSON):
        print(JSON['sha'])
        print(JSON['author']['login'])
        print(JSON['commit']['author']['date'])
        self.sha = JSON['sha']
        self.author_login = JSON['author']['login']
        self.date = JSON['commit']['author']['date']

class GitHubCollaborator:
    def __init__(self, JSON):
        print(JSON['login'])
        self.login = JSON['login']

class GitHubRepoInfo:
    pass

class RepositoryFile:
    pass