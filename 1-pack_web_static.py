#!/usr/bin/python3
"""This module defines how to compress before sending"""
from fabric.api import local
from os import path
from time import strftime as time


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
