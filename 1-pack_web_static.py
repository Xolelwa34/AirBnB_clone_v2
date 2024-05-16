#!/usr/bin/python3
"""
A function that reduces a folder in app
"""
from datetime import datetime
from fabric.api import local


def do_pack():
    """ Generates archive from the web static folder"""

    time = datetime.now()
    archive = 'web_static_' + time.strftime("%Y%m%d%H%M%S") + '.' + 'tgz'
    local('mkdir -p versions')
    create = local('tar -cvzf versions/{} web_static'.format(archive))
    if create is not None:
        return archive
    else:
        return None
