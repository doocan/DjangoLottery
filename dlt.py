import os
import django
from django.conf import settings

settings.configure(
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend',
    EMAIL_HOST = 'smtp.qq.com',
    EMAIL_PORT = 465,
    EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER'),
    EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD'),
    EMAIL_USE_SSL = True,
    EMAIL_USE_LOCALTIME = True,
    EMAIL_TO = ['i@qtitan.com'],
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ],
            },
        },
    ]
)

django.setup()


import random
import time
from datetime import datetime

from django.template import Context, Template
from django.core.mail import send_mail


def create(count=5):
    dlts = []
    for i in range(count):
        front = sorted(random.sample(range(1, 36), 5))
        back = sorted(random.sample(range(1, 13), 2))

        time.sleep(random.random())

        dlt = {
            'a': front[0], 
            'b': front[1],
            'c': front[2],
            'd': front[3],
            'e': front[4],
            'f': back[0],
            'g': back[1]
        }
        dlts.append(dlt)

    return dlts


template = Template('''
  <table border="2">
      <caption>大乐透 {{ now|date:'Y-m-d H:i'|safe }}</caption>
      <tr>
          <th>前区</th>
          <th>后区</th>
      </tr>
      {% for dlt in dlts %}
          <tr>  
              <td>{{ dlt.a }} {{ dlt.b }} {{ dlt.c }} {{ dlt.d }} {{ dlt.e }}</td>
              <td>{{ dlt.f }} {{ dlt.g }}</td>
          </tr>
      {% endfor %}
  </table>
''')

dlts = create()

context = Context({
    'now': datetime.now(),
    'dlts': dlts
})

msg = template.render(context)


send_mail('[天降祥瑞]',
          'Ritch Text Error',
          'man_hattan@qq.com',
          settings.EMAIL_TO,
          fail_silently=False,
          html_message=msg
)
