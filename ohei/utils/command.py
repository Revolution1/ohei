import shlex
from pprint import pprint
from subprocess import Popen, PIPE


def exec_cmd(cmd):
    if isinstance(cmd, str):
        cmd = shlex.split(cmd)
    sh = True if len(cmd) == 1 else False
    proc = Popen(cmd, stdout=PIPE, stderr=PIPE, shell=sh)
    out, err = proc.communicate()
    if proc.returncode == 0:
        return str(out).strip(), str(err).strip()
    else:
        raise Exception("stderr: %s" % str(err))


if __name__ == '__main__':
    pprint(exec_cmd('ls'))
    pprint(exec_cmd('python --version'))
    pprint(exec_cmd(['/bin/ls', '--aaa']))
    pprint(exec_cmd('dmidecode'))
