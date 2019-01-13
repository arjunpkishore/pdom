# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.db import models

# Create your models here.
class app_log(models.Model):
    transaction_id = models.IntegerField(blank=True)
    message = models.TextField(blank=False)
    entry_time = models.DateTimeField(default=datetime.now(), blank=False)
    def __str__(self):
        return('{}: {}'.format(self.entry_time, self.message))
