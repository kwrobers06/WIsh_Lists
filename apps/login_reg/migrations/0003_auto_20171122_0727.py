# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-11-22 07:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login_reg', '0002_item'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='users',
            new_name='user',
        ),
    ]
