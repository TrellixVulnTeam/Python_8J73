# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-17 22:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login_register', '0008_auto_20180417_1535'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='birthday',
        ),
    ]
