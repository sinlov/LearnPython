# For python language playground

## runtime

- python runtime suggest to use docker

```bash
# use makefile to build images
$ make dockerImagesBuild
```

- change proxy of pip before run `make dockerImagesBuild` at file [./Dockerfile](./Dockerfile)

```Dockfile
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple \
```

- install more package can change file [./requirements.txt](./requirements.txt)

> must use `make dockerImagesBuild` after change requirements.txt 

## use in PyCharm

- in `settings` -> `Python Interpreter`
- Click the `gear button` on the right, and press `add..`

![runtime-1.png](doc/runtime-1.png)

- select `Docker Compose`

![runtime-2.png](doc/runtime-2.png)

> if `Server:` is empty can click `New...` button add docker engine

- select `Services:`, by file [./docker-compose.yml](./docker-compose.yml)
- add some `Enviroment variables:`

![runtime-3.png](doc/runtime-3.png)

- then pass `Ok`