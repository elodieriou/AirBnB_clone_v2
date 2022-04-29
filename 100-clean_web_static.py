#!/usr/bin/python3
"""This module defines:
 - how to compress before sending
 - how to deploy an archive on a server
 - how to do a full deployment
 - how to keep clean a server"""
from fabric.api import local, put, run, env, lcd, cd
from os import path, listdir
from time import strftime as time
env.hosts = ['34.139.85.9', '35.231.199.91']


def do_pack():
    """This method defines a script that generates a .tgz archive from the
    contents of the 'web_static' folder of the AirBnB Clone repo"""

    if path.exists("versions/") is False:
        local("mkdir versions/")
    try:
        file_path = "versions/web_static_{}{}{}{}{}{}.tgz".format(time("%Y"),
                                                                  time("%m"),
                                                                  time("%d"),
                                                                  time("%H"),
                                                                  time("%M"),
                                                                  time("%S"))
        local("tar -cvzf {} web_static".format(file_path))
        return file_path

    except Exception:
        return None


def do_deploy(archive_path):
    """This method defines a script that distributes an archive to
    a server web"""
    if path.exists(archive_path) is False:
        return False

    try:
        file_name = archive_path.split("/")
        put("{}/{}".format(file_name[0], file_name[1]),
            "/tmp/{}".format(file_name[1]))
        del_ext = file_name[1].split(".")
        run("mkdir -p /data/web_static/releases/{}/".format(del_ext[0]))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
            .format(file_name[1], del_ext[0]))
        run("rm /tmp/{}".format(file_name[1]))
        run("mv /data/web_static/releases/{}/web_static/*\
        /data/web_static/releases/{}/".format(del_ext[0], del_ext[0]))
        run("rm -rf /data/web_static/releases/{}/web_static"
            .format(del_ext[0]))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
            .format(del_ext[0]))
        return True

    except Exception:
        return False


def deploy():
    """This method define a script that creates and distributes an archive to
    a web server"""
    create_archive = do_pack()
    if create_archive is None:
        return False
    deployment = do_deploy(create_archive)
    return deployment


def do_clean(number=0):
    """This method defines a script that deletes out-of-date archives"""
    num = int(number)
    if num == 0:
        num = 1

    with lcd("versions"):
        list_file = local("ls -1t", capture=True)
        old_version = list_file.split("\n")
        to_delete = old_version[num:]

        for file in to_delete:
            local("rm {}".format(file))

    with cd("/data/web_static/releases/"):
        list_directory = run("ls -1t")
        old_version = list_directory.split("\n")
        to_delete = old_version[num:]

        copy_list = to_delete.copy()
        for directory in copy_list:
            if directory == "test":
                copy_list.pop(directory)
            run("rm -rf {}".format(directory))
