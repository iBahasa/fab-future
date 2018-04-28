from __future__ import with_statement
from fabric.api import *
from fabric.contrib.console import confirm

def git_status():
    local("git status")

def git_add():
    local("git add -A")

def git_commit(name="fab"):
    local("git commit -nm '%s'" % name)

def git_push():
    local("git push origin master")

def deploy(commit="fab commit"):
    git_status()
    git_add()
    git_commit(name=commit)
    git_push()
