FROM python:2.7.18-buster

RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple

WORKDIR /usr/src/app