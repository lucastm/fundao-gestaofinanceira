# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-05 14:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GestaoFinanceira', '0003_auto_20170405_1121'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='cnpj',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='pessoa',
        ),
        migrations.AlterField(
            model_name='pagamento',
            name='ano',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='pagamento',
            name='mes',
            field=models.IntegerField(choices=[(1, 'Janeiro'), (2, 'Fevereiro'), (3, 'Março'), (4, 'Abril'), (5, 'Maio'), (6, 'Junho'), (7, 'Julho'), (8, 'Agosto'), (9, 'Setembro'), (10, 'Outubro'), (11, 'Novembro'), (12, 'Dezembro')], null=True),
        ),
    ]
