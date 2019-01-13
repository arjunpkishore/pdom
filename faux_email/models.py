# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from datetime import datetime
# Create your models here.

class f_email(models.Model):
    e_from = models.CharField(max_length=50, blank=False)
    e_to = models.CharField(max_length=50, blank=False)
    e_cc = models.CharField(max_length=50, blank=True)
    e_bcc = models.CharField(max_length=50, blank=True)
    e_subject = models.CharField(max_length=50, blank=True)
    e_body = models.TextField(blank=False)
    e_sent_time = models.DateTimeField(default=datetime.now(), blank=False)

    def __str__(self):
        return('From: {}\tSubject:{}'.format(self.e_from, self.e_subject))
    class Meta:
        verbose_name_plural = 'eMails'
        verbose_name = 'eMail'
        ordering = ['-e_sent_time']
