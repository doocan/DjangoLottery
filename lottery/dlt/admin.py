from django.contrib import admin

from .models import Tag, DLT, ActDlt


admin.site.register(Tag)
admin.site.register(DLT)
admin.site.register(ActDlt)
