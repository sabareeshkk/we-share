# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-15 23:01
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mess', '0008_auto_20170615_0128'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('description', models.CharField(max_length=50)),
                ('date', models.DateTimeField()),
                ('settled', models.BooleanField(default=False)),
            ],
        ),
        migrations.RenameModel(
            old_name='MessGroup',
            new_name='WSGroup',
        ),
        migrations.RemoveField(
            model_name='member',
            name='group',
        ),
        migrations.AddField(
            model_name='bill',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 15, 23, 1, 18, 596062, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='member',
            name='date',
            field=models.DateTimeField(),
        ),
        migrations.AddField(
            model_name='transaction',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mess.WSGroup'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='lender',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lender', to='mess.Member'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='receiver',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to='mess.Member'),
        ),
    ]
