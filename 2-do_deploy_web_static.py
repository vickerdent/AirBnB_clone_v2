#!/usr/bin/python3
"""Script (based on the file 1-pack_web_static.py) that distributes an
archive to your web servers, using the function do_deploy.
"""
from fabric.context_managers import cd, hide,\
        settings, show, path, prefix, lcd, quiet, warn_only,\
        remote_tunnel, shell_env
from fabric.decorators import hosts, roles,\
        runs_once, with_settings, task, serial, parallel
from fabric.operations import require, prompt,\
        put, get, run, sudo, local, reboot, open_shell
from fabric.state import env, output
from fabric.utils import abort, warn, puts, fastprint
from fabric.tasks import execute
from datetime import datetime
import os
