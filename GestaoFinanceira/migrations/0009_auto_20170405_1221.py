# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-05 15:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GestaoFinanceira', '0008_auto_20170405_1206'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='CPF/CNPJ',
            new_name='cpfCnpj',
        ),
    ]
