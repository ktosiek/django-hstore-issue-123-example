# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import example.fields
import django_hstore.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HandInHStore',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('data', django_hstore.fields.DictionaryField(null=True, editable=False)),
                ('native_hand', example.fields.HandField()),
            ],
        ),
    ]
