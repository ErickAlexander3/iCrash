# Generated by Django 2.1.5 on 2019-03-19 21:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_auto_20190227_2308'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='info',
        ),
    ]
