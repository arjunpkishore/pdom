# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
import uuid
from django.db import models

# Create your models here.
class verification_token(models.Model):
    token = models.UUIDField(default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(default=datetime.now(), blank=False)
    utilized = models.BooleanField(default=False, blank=True)
    utilized_at = models.DateTimeField(null=True, blank=True)
    def __str__(self):
        return('{} : {}'.format(self.token.hex, 'Utilized' if self.utilized else 'Not Utilized'))
