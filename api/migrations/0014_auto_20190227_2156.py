# Generated by Django 2.1.5 on 2019-02-28 05:56

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_auto_20190227_1849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crashlog',
            name='log',
            field=django.contrib.postgres.fields.jsonb.JSONField(),
        ),
    ]
