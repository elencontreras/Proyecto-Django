from fabric.api import task, run

@task

def info_sistema():
	run('uname -a')