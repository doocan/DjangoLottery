# -*- coding: utf-8 -*-

import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lottery.settings")

import django

django.setup()

from datetime import datetime

import requests
from fake_useragent import UserAgent
from celery import shared_task

from dlt.models import Tag, ActDlt


url = "http://www.js-lottery.com/PlayZone/ajaxLottoData"


@shared_task
def dlt_spider():
    num = get_current_num()
    Tag.objects.create(num=num)

    num = Tag.objects.last().num
    dlt_crawl(num)


# 判断目前 yikaijiang 的是第几期
def get_current_num():
    data = {
        'current_page': 1,
        'all_count': 0,
        'num': None
    }
    headers = {'user-agent': UserAgent().random}
    r = requests.post(url, data=data, headers=headers)
    num = r.json().get('items')[0].get('num')
    return int(num)


def dlt_crawl(num):
    # try:
    #     num = Tag.objects.last().num + 1
    # except Exception:
    #     num = get_current_num() + 1

    data = {
        'current_page': 1,
        'all_count': 0,
        'num': num
    }
    headers = {'user-agent': UserAgent().random}
    r = requests.post(url, data=data, headers=headers)
    try:
        items = r.json().get('items')[0]
    except Exception:
        return None

    ActDlt.objects.create(a=int(items.get('one')),
                          b=int(items.get('two')),
                          c=int(items.get('three')),
                          d=int(items.get('four')),
                          e=int(items.get('five')),
                          f=int(items.get('six')),
                          g=int(items.get('seven')),
                          num=num,
                          published=datetime.fromtimestamp(int(items.get('time_publish'))))
