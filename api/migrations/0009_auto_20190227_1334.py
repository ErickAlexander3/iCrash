# Generated by Django 2.1.5 on 2019-02-27 21:34

import django.contrib.postgres.fields
import django.contrib.postgres.fields.hstore
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20190227_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='emergency_contacts',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.hstore.HStoreField(), default=list, size=None),
        ),
    ]
