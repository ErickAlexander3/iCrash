# Generated by Django 2.1.5 on 2019-02-27 21:44

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20190227_1334'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='emergency_contacts',
        ),
        migrations.AddField(
            model_name='userinfo',
            name='contacts',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=dict),
        ),
    ]
