#!/usr/bin/python3
"""This module defines how to compress before sending"""
from fabric.api import local
from os import path
from time import strftime


def do_pack():
    """This method defines a script that generates a .tgz archive from the
    contents of the 'web_static' folder of the AirBnB Clone repo"""

    if path.exists("versions/") is False:
        local("mkdir versions/")
    local("tar -cvzf versions/web_static_{}{}{}{}{}{}.tgz web_static"
          .format(strftime("%Y"), strftime("%m"), strftime("%d"),
                  strftime("%H"), strftime("%M"), strftime("%S")))
