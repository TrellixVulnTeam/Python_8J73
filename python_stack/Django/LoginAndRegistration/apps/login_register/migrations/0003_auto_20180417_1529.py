# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-17 22:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_register', '0002_user_birthday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birthday',
            field=models.CharField(max_length=11),
        ),
    ]
