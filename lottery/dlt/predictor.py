import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lottery.settings")

import django

django.setup()

import time
import random

from push.tasks import dlt_push
from .models import DLT, Tag


try:
    num = Tag.objects.last().num
except:
    num = 0

def create(num=num, count=5):
    for i in range(count):
        front = sorted(random.sample(range(1, 36), 5))
        back = sorted(random.sample(range(1, 13), 2))
        dlt = DLT.objects.create(a=front[0], 
                                 b=front[1],
                                 c=front[2],
                                 d=front[3],
                                 e=front[4],
                                 f=back[0],
                                 g=back[1],
                                 num=num)
        time.sleep(random.random())
        
    dlt_push.delay(num, count)
