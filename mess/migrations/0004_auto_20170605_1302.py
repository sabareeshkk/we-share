# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-05 13:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mess', '0003_auto_20170605_1253'),
    ]

    operations = [
        migrations.RenameField(
            model_name='add_bill',
            old_name='mess_expenses',
            new_name='other_expenses',
        ),
    ]
