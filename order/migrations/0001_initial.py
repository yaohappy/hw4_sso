# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('order_id', models.CharField(max_length=20)),
                ('customer', models.CharField(max_length=20)),
                ('item', models.CharField(max_length=20)),
            ],
        ),
    ]
