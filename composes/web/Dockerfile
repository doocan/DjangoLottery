FROM python:3.6.2

USER root

ENV PIP https://pypi.douban.com/simple

COPY requirements.txt /root
  
RUN  pip install -i $PIP -U pip && \
     pip install -i $PIP -r /root/requirements.txt