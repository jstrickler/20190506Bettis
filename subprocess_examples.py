#!/usr/bin/env python
from subprocess import run, PIPE, CalledProcessError

proc = run("netstat -an", shell=True)
print(proc.returncode)
print(proc)
print('-' * 60)

proc = run("netstat -an", shell=True, stdout=PIPE, stderr=PIPE)
if proc.returncode == 0:
    for line in proc.stdout.decode().splitlines():
        if 'ESTAB' in line:
            print(line)
    print(proc.stderr.decode())


