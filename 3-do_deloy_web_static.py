#!/usr/bin/python3
"""Web application deployment for web static with Fabric"""

from fabric.api import env, local, put, run
from datetime import datetime
from os.path import exists, isdir
import os

env.hosts = ['35.237.96.82', '54.164.136.88']


def do_pack():
    """Archives the web static files"""
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if not isdir("versions"):
            local("mkdir versions")
        filename = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(filename))
        return filename
    except Exception as ex:
        print(f"Error in do_pack: {ex}")
        return None


def do_deploy(archive_path):
    """Deploys web static with Fabric"""
    if not exists(archive_path):
        return False

    try:
        filename = archive_path.split("/")[-1]
        no_ext = filename.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('sudo mkdir -p {}{}/'.format(path, no_ext))
        run('sudo tar -xzf /tmp/{} -C {}{}/'.format(filename, path, no_ext))
        run('sudo rm /tmp/{}'.format(filename))
        run('sudo mv {0}{1}/web_static/* {0}{1}/'.format(path, no_ext))
        run('sudo rm -rf {}{}/web_static'.format(path, no_ext))
        run('sudo rm -rf /data/web_static/current')
        run('sudo ln -s {}{}/ /data/web_static/current'.format(path, no_ext))
        print("New version deployed!")
        return True
    except Exception as ex:
        print(f"Error in do_deploy: {ex}")
        return False


def deploy():
    """Creates and distributes an archive to the web servers"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
