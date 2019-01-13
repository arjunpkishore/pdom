# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from datetime import datetime
# Create your models here.
class f_fim(models.Model):
    fim_group = models.CharField(max_length=100, blank=False)
    fim_owner = models.CharField(max_length=50, blank=False)
    fim_requestor = models.CharField(max_length=50, blank=False)
    created_at = models.DateTimeField(default=datetime.now(), blank=False)
    class Meta:
        verbose_name_plural='FIMs'
        verbose_name = 'FIM'
        
