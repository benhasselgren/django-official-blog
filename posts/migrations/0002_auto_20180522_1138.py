# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-22 11:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='published',
            new_name='published_date',
        ),
    ]
