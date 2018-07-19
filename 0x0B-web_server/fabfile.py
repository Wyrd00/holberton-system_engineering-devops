#!/usr/bin/python2.7
# pack:creates a tar gzipped archive of the current directory
# deploy:upload archive to remote server in /tmp/
#       :creates directory /tmp/holbertonwebapp
#       :untars archive into /tmp/holbertonwebapp
# clean: delete tar file on local machine


from fabric.api import *


#env.hosts = ["35.237.190.7"]
env.user = "ubuntu"
#env.password = ""
#env.key_filename = "~/.ssh/holberton"


def pack():
        """
        pack: creates a tar gzipped archive of the current directory
              and place in the local directory
        """
        local("tar --exclude='*.tar.gz' -cvzf holbertonwebapp.tar.gz .")


def deploy():
        """
        deploy: upload archive to remote server in /tmp/
                creates directory /tmp/holbertonwebapp
                untars archive into /tmp/holbertonwebapp
        """
        run("mkdir /tmp/holbertonwebapp")
        put("holbertonwebapp.tar.gz", "/tmp/holbertonwebapp")
        run("cd /tmp/ && tar -xvf holbertonwebapp.tar.gz -C /holbertonwebapp")


def clean():
        """
        clean: delete tar file on local machine
        """
        local("rm holbertonwebapp.tar.gz")
