#!/usr/bin/python3
"""
a Fabric script that deletes out-of-date archives
execute: fab -f 100-clean_web_static.py do_clean:number=2
    -i ssh-key -u ubuntu > /dev/null 2>&1
"""
import os
from fabric.api import *

env.hosts = ['18.234.253.252', '52.91.153.152']


def do_clean(number=0):
    """
    Deletes out-of-date archives.

    Args:
        number (int): Number of archives to keep. If 0 or 1, keeps only the,
                      most recent. If 2, keeps the two most recent, and so on.
    """
    number = 1 if int(number) == 0 else int(number)

    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archives]
