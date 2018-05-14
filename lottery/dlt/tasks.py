import random

from celery import task, shared_task
#from lottery import celery_app as app

from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.utils import timezone
from dlt.models import DLT 
from dlt.utils import get_next_num

# random.seed(19900914)


@shared_task
def dlt_create():
    front = sorted(random.sample(range(1, 36), 5))
    back = sorted(random.sample(range(1, 13), 2))

    num = get_next_num()

    dlt_list = []
    
    for i in range(5):
        dlt = DLT.objects.create(a=front[0], 
                                 b=front[1],
                                 c=front[2],
                                 d=front[3],
                                 e=front[4],
                                 f=back[0],
                                 g=back[1],
                                 num=num)
        dlt_list.append(dlt)

    dlt_created.delay(dlt_list)


@shared_task
def dlt_created(dlt_list):
    msg = render_to_string('dlt_template.html', 
                           {'A': dlt_list[0],
                            'B': dlt_list[1],
                            'C': dlt_list[2],
                            'D': dlt_list[3],
                            'E': dlt_list[4],
                            'now': timezone.now()})
    mail_sent = send_mail('[天降祥瑞]',
                          'Ritch Text Error',
                          'man_hattan@qq.com',
                          ['i@qtitan.com'],
                          fail_silently=False,)
    return mail_sent