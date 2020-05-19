FROM python:2.7.18-buster

COPY requirements.txt ./

RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple \
    && pip install --no-cache-dir -r requirements.txt

WORKDIR /usr/src/app