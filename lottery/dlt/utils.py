# -*- coding: utf-8 -*-

import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lottery.settings")

import random
import datetime

import django
from django.conf import settings
from django.core.mail import send_mail
from mako.lookup import TemplateLookup
from mako.template import Template

django.setup()

# random.seed(19900914)
# directories = [os.path.join(settings.BASE_DIR, 'dlt', 'templates')]
# for i in settings.TEMPLATES[0].get('DIRS'):
#     directories.append(i)
#
# mylookup = TemplateLookup(directories=directories)

class Task(object):
    def __init__(self):
        pass

    def message(self):
        template = Template('<%include file="dlt_template.html" />', lookup=mylookup)

    def content(self):
        front = sorted(random.sample(range(1, 36), 5))
        back = sorted(random.sample(range(1, 13), 2))
        return front, back

