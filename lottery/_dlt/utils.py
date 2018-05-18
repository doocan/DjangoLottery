# -*- coding: utf-8 -*-

import os


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lottery.settings")


import django

django.setup()

import random
import datetime

import requests
from fake_useragent import UserAgent
from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.utils import timezone

# random.seed(19900914)
# directories = [os.path.join(settings.BASE_DIR, 'dlt', 'templates')]
# for i in settings.TEMPLATES[0].get('DIRS'):
#     directories.append(i)
#
# mylookup = TemplateLookup(directories=directories)

# 判断目前正在售卖的是第几期
def get_next_num():
    url = "http://www.js-lottery.com/PlayZone/ajaxLottoData"
    data = {
        'current_page': 1,
        'all_count': 0,
        'num': None
    }
    headers = {'user-agent': UserAgent().random}
    r = requests.post(url, data=data, headers=headers)
    num = r.json().get('items')[0].get('num')
    return int(num)+1
