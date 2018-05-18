import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lottery.settings")

import django

# django.setup()


from celery import task, shared_task

from django.conf import settings
from django.db.utils import InterfaceError
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils import timezone

from dlt.models import DLT


@shared_task
def dlt_push(num, count):
    django.setup()
    try:
        # ordering = ['-created']
        dlts = DLT.objects.filter(num=num)[:count]
    except IndexError as e:
        raise InterfaceError(f'There must be {count} items.')

    msg = render_to_string('dlt_template.html', 
                           {'dlts': dlts,
                            'now': timezone.now()})
    mail_sent = send_mail('[天降祥瑞]',
                          'Ritch Text Error',
                          'man_hattan@qq.com',
                          settings.EMAIL_TO,
                          fail_silently=False,
                          html_message=msg)
    return mail_sent


@shared_task
def dlt_status_push(num):
    try:
        # ordering = ['-created']
        dlts = DLT.objects.filter(num=num)
    except IndexError as e:
        raise e

    msg = render_to_string('dlt_status_template.html', 
                          {'dlts': dlts,
                           'now': timezone.now()})
    mail_sent = send_mail('[天降kaijiang]',
                          'Ritch Text Error',
                          'man_hattan@qq.com',
                          settings.EMAIL_TO,
                          fail_silently=False,
                          html_message=msg)
    return mail_sent
