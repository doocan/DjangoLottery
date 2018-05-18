import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lottery.settings")

import django

django.setup()


import random

from push.tasks import dlt_push
from .models import DLT, Tag


num = Tag.objects.last().num

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
    dlt_push.delay(num, count)
