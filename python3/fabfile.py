#!/usr/local/homebrew/bin/python3

from fabric import Connection, task
from invoke import run

@task
def deploy(c):
    with Connection('test@10.211.55.5') as c:
        c.run("rm -rf giligili")
        c.run("git clone https://github.com/jinyuyoulong/giligili.git", pty=True)
        c.put("docker-compose.yml", "giligili/docker-compose.yml")
        c.run("cd giligili && docker-compose build && docker-compose rm -fsv && docker-compose up --build -d", pty=True)
        c.run("sleep 15 && docker logs -f gili-api")

@task
def init(c):# 参数 c 是干嘛的
	run('echo hello')

# doc http://docs.fabfile.org/en/2.5/getting-started.html
# apt install python-pip
# pip install fabric -i http://mirrors.aliyun.com/pypi/simple/
# fab deploy

# 转换为 shell 命令执行
from invoke import run
run('uname -s')
run('echo hello')


