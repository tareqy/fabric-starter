#!/usr/local/bin/python
from fabric.api import *

# SSH Users
env.user = 'root'

# Servers List
env.hosts = [
	'server-1',
	'server-2',
]

# Simple Fabric Task
@task
def uptime():
	"""
	shows system uptime
	"""
	run("uptime")
