# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-02-16 14:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='login',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('id_card', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('sex', models.CharField(max_length=5)),
            ],
        ),
    ]
