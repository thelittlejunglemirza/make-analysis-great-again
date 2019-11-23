import requests
import json
import os
import subprocess
from data_collection.models import GitHubCollaborator, GitHubCommit


GITHUB_API_BASE_URI = 'https://api.github.com/repos/'

class GitHubClient:
    def __init__(self, username, repo):
        self.username = username
        self.repo = repo
        self.collaborators = []

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
        r = requests.get('{}{}/{}/commits?page={}'.format(GITHUB_API_BASE_URI, self.username, self.repo, page))
        if r.ok:
            return r.json()

    def get_commit_info(self, sha):
        r = requests.get('{}{}/{}/commits/{}'.format(GITHUB_API_BASE_URI, self.username, self.repo, sha))
        if r.ok:
            return r.json()
          
    def get_commit_changes(self, folder_path, sha):
        if os.path.exists(folder_path):
            if not os.path.exists('{}/{}.txt'.format(folder_path, sha)):
                arch = subprocess.check_output('cd {} && git show {}'.format(folder_path, sha), shell=True)
                f = open("data/{}.txt".format(sha), "w+")
                f.write(arch.decode("utf-8"))
                f.close()

    def clean_github_env(self):
        os.system('rm -r data')

    def setup_github_env(self, url):
        if not os.path.exists('data'):
            os.system('mkdir data')
        folder_path = 'data/{}'.format(url.split('/')[len(url.split('/')) - 1].split('.')[0])
        if not os.path.exists(folder_path):
            subprocess.call('cd data && git clone {}'.format(url), shell=True);
        return folder_path
