#!/usr/bin/python3
"""Compress before sending"""
from fabric.api import local, env, put, run
from datetime import datetime
import os
import os.path as path

# -i my_ssh_private_key -u ubuntu
env.hosts = ['35.237.217.126', '35.229.75.225']

def do_pack():
    """script that generates a .tgz archive"""
    try:
        now = datetime.now()
        local('mkdir -p versions/')
        dt_string = now.strftime("%Y%m%d%H%M%S")
        filename = "web_static_" + dt_string + ".tgz"
        local('tar -cvzf versions/{} web_static/'.format(filename))
        path = './versions/{}'.format(filename)
        print("web_static packed: {} ->{}Bytes"
              .format(path, os.path.getsize(path)))
    except:
        return None

def do_deploy(archive_path):
    """function2"""
    now = datetime.now()
    dt_string = now.strftime("%Y%m%d%H%M%S")
    path = "web_static" + dt_string + ".tgz"
    path2 = "web_static" + dt_string
    if path.exists(archive_path):
        put(archive_path, "/home/ubuntu/pruebascarlitos/") #cambiar ruta absoluta por ruta de las task
        run("sudo mkdir -p  /data/web_static/releases/{}/".format(path2))
        run("sudo tar -xzf /home/ubuntu/pruebascarlitos/{} -C /data/web_static/releases/{}/".format(path, path2))
        run("sudo rm /home/ubuntu/pruebascarlitos/{}".format(path))
        run("sudo mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/".format(path2, path2))
        run("sudo rm -rf /data/web_static/releases/{}/web_static".format(path2))
        run("sudo rm -rf /data/web_satic/current")
        run("sudo ln -s /data/web_static/releases/{}/ /data/web_static/current".format(path2))
        return True


    else:
        print("Fallooo :c")
        return False

if __name__ == "__main__":
    do_deploy()
