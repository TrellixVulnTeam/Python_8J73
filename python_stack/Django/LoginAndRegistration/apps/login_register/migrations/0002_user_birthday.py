# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-17 22:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_register', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='birthday',
            field=models.DateField(),
            preserve_default=False,
        ),
    ]
