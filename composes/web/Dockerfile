FROM python:3.6.2

USER root

ENV PIP https://pypi.douban.com/simple

COPY requirements.txt /root
COPY sqlite3/* /usr/local/sqlite3/

RUN  echo 'export PATH="/usr/local/sqlite3:$PATH"' >> /root/.bashrc && \
     exec $SHELL && \
     pip install -i $PIP -U pip && \
     pip install -i $PIP -r /root/requirements.txt