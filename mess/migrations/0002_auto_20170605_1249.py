# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-05 12:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mess', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Admin_user',
            new_name='Add_bills',
        ),
        migrations.RenameModel(
            old_name='Mess_data',
            new_name='Mess_member',
        ),
    ]
