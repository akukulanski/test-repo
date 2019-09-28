from travispy import TravisPy
import os
#os.environ['GITHUB_TOKEN']
t = TravisPy.github_auth(os.environ['GITHUB_TOKEN'])
print('User: ', t.user().login)
repo = t.repo('akukulanski/test-repo')
print('Repo: ', repo)
print('Repo state: ', repo.state)


