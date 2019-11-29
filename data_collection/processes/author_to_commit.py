import json, os
dir = directory_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def get_author_to_commits_map():
    author_to_commit = {}
    try:
        commits_detailed_json_file = os.path.join(dir, 'data/commits_detailed.json')
        with open(commits_detailed_json_file, 'r') as my_file:
            data = my_file.read()
        # parsing detailed file
        obj = json.loads(data)
        for o in obj:
            temp_obj = {'sha': o['sha'], 'date': o['commit']['author']['date'], 'files': []}
            login = o['author']['login']
            for file in o['files']:
                temp_obj['files'].append({
                    'filepath': file['filename'],
                    'additions': file['additions'],
                    'deletions': file['deletions'],
                })
            if login in author_to_commit:
                author_to_commit[login].append(temp_obj)
            else:
                author_to_commit[login] = []
                author_to_commit[login].append(temp_obj)
    except Exception as e:
        print('caught error in reading detailed data: ' + str(e))

    return author_to_commit
