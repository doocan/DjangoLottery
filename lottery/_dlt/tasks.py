import os


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lottery.settings")


import django

django.setup()


import random

from celery import task, shared_task
# from lottery import celery_app as app
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils import timezone
from django.db.utils import InterfaceError
from dlt.models import DLT 
from dlt.utils import get_next_num

# random.seed(19900914)


@shared_task
def dlt_create():
    num = get_next_num()
    
    for i in range(5):
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

    dlt_created.delay(num)


@shared_task
def dlt_created(num):
    try:
        dlts = DLT.objects.filter(num=num)[:5]
    except Exception as e: 
        raise InterfaceError('There must be 5 items.')

    msg = render_to_string('dlt_template.html', 
                           {'A': dlts[0],
                            'B': dlts[1],
                            'C': dlts[2],
                            'D': dlts[3],
                            'E': dlts[4],
                            'now': timezone.now()})
    mail_sent = send_mail('[天降祥瑞]',
                          'Ritch Text Error',
                          'man_hattan@qq.com',
                          settings.EMAIL_TO,
                          fail_silently=False,
                          html_message=msg)
    return mail_sent