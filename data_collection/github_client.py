import requests
import json
from data_collection.models import GitHubCollaborator, GitHubCommit


GITHUB_API_BASE_URI = 'https://api.github.com/repos/'

class GitHubClient:
    def __init__(self, username, repo):
        self.username = username
        self.repo = repo
        self.collaborators = []
        self.commits = []

    def get_repo_info(self):
        # repository has to be public
        r = requests.get('{}{}/{}'.format(GITHUB_API_BASE_URI, self.username, self.repo))
        if (r.ok):
            return r.json()

    def get_collaborators(self):
        r = requests.get('{}{}/{}/contributors'.format(GITHUB_API_BASE_URI, self.username, self.repo)).json()
        # if (r.ok):
        #     return json.loads(r.content)
        for JSONObject in r:
            collaborator = GitHubCollaborator(JSONObject)
            self.collaborators.append(collaborator)
        # for collaborator in r.content:
        #    GitHubCollaborator(r.content)



    def get_commits(self, page=1):
        r = requests.get('{}{}/{}/commits?page={}'.format(GITHUB_API_BASE_URI, self.username, self.repo, page)).json()
        # if (r.ok):
        #     return r.json()
        for JSONObject in r:
            commit = GitHubCommit(JSONObject)
            self.commits.append(commit)
