# Generated by Django 2.0.5 on 2018-05-21 10:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dlt', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ('num',)},
        ),
    ]
