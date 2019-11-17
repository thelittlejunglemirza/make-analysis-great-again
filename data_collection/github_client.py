import requests
import json
class GitHubClient:
    def __init__(self, username, repo):
        self.username = username
        self.repo = repo

    def get_repo_info(self):
        #GET /repos/:owner/:repo/
        # repository has to be public
        username = 'django'
        repository = 'django'
        r = requests.get('https://api.github.com/repos/{}/{}'.format(self.username, self.repository))
        if (r.ok):
            print(r.json())
            return r.json()

        pass

    def get_collaborators(self):
        #GET /repos/:owner/:repo/contributors
        r = requests.get('https://api.github.com/repos/{}/{}/contributors'.format(self.username, self.repository))

        if (r.ok):
            print(r.json())
            return r.json()

        pass

    def get_commits(self):

        r = requests.get('https://api.github.com/repos/{}/{}/commits'.format(self.username, self.repository))
        if (r.ok):
            print(r.json())
            return r.json()

        #GET / repos /: owner /:repo / commits
        pass
