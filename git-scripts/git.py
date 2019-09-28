import subprocess
import re

def run_command(cmd):
    cmd_ = cmd.split(' ')
    result = subprocess.run(cmd_, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {'return_value': result.returncode,
            'stdo': result.stdout.decode('utf-8'),
            'stde': result.stderr.decode('utf-8'),
           }


def get_diff(other):
    ret = run_command(f'git diff --name-only {other}')
    return [f for f in ret['stdo'].split('\n') if f]

filtrar = lambda regex, lista: list(filter(re.compile(regex).match, lista))

branch = 'b1'
files = get_diff(branch)
print('Diff: {}'.format(files))
filtered_files = filtrar(r'.*.md', files)
