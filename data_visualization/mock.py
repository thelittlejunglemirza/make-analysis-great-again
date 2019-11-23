class DummyCommit:
    def __init__(self, collaborator, module, change):
        self.collaborator = collaborator
        self.module = module
        self.change = change


class DummyCollaborator:
    def __init__(self, login):
        self.login = login


class DummyModule:
    def __init__(self, name):
        self.name = name

