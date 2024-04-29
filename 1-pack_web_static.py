#!/usr/bin/python3
"""
A function that reduces a folder in app
"""
from datetime import datetime
from fabric.api import local


def do_pack():
    """ Generates archive from the web static folder"""
    try:
        local("mkdir -p versions")
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        rout = "versions/web_static_{}.tgz".format(date)
        _gzip = local("tar -cvzf {} web_static".format(rout))
        return rout
    except Exception:
        return None
