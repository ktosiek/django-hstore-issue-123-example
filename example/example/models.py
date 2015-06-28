from django.db import models
from django_hstore import hstore
from .fields import HandField


class HandInHStore(models.Model):
    data = hstore.DictionaryField(schema=[
        {
            'name': 'hand',
            'class': HandField,
        },
    ])
