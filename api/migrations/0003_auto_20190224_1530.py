# Generated by Django 2.1.5 on 2019-02-24 23:30
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_crashlog_device_userinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='serial',
            field=models.TextField(unique=True),
        ),
    ]