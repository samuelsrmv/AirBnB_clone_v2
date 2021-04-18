#!/usr/bin/python3
"""Compress before sending"""
from fabric.api import local, env, put, run
from datetime import datetime
import os
import os.path as path

# -i my_ssh_private_key -u ubuntu
env.hosts = ['35.237.217.126']

def do_deploy(archive_path):
    """function2"""
    if path.exists(archive_path):
        put(archive_path, "/home/ubuntu/pruebascarlitos/") #cambiar ruta absoluta por ruta de las task
        run("sudo mkdir -p  /data/web_static/releases/web_static_20210418131carlitos/")
        run("sudo tar -xzf /home/ubuntu/pruebascarlitos/web_static_20210418131854.tgz -C /data/web_static/releases/web_static_20210418131carlitos/")





    else:
        print("Fallooo :c")
        return False

if __name__ == "__main__":
    do_deploy()
