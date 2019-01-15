# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from token_mgmt.models import Verification_Token
from datetime import datetime

# Create your models here.

class Request_Targets(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=False)
    type = models.CharField(max_length=100, blank=False)
    parent_obj = models.ForeignKey('self', blank=True)
    approver = models.ManyToManyField(User, related_name='approving_user')
    permission_api = models.ForeignKey('Permission_Api')
    created_by = models.ForeignKey(User, related_name='creating_user')
    updated_by = models.ForeignKey(User, related_name='updating_user')
    created_at = models.DateTimeField(default=datetime.now())
    updated_at = models.DateTimeField(default=datetime.now())
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Request Target'
        verbose_name = 'Request Target'



class Access_Requests(models.Model):
    requestor = models.ForeignKey(User)
    request_target = models.ForeignKey('Request_Targets')
    request_status = models.CharField(max_length=200)
    access_FIM = models.CharField(max_length=200)
    access_FIM_exists = models.BooleanField(default=False)
    access_approved = models.CharField(max_length=200)
    approval_token = models.OneToOneField(Verification_Token)
    created_at = models.DateTimeField(default=datetime.now())
    updated_at = models.DateTimeField(default=datetime.now())
    def __str__(self):
        return ('Request {}, Requested by: {}'.format(self.id, self.requestor))
    class Meta:
        verbose_name_plural = 'Access Request'
        verbose_name = 'Access Request'

class Permission_Api(models.Model):
    name = models.CharField(max_length=200)
    api_endpoint = models.CharField(max_length=500)
    api_token = models.CharField(max_length=500)
    api_headers = models.CharField(max_length=500)
    api_body = models.TextField()
    created_by = models.ForeignKey(User)
    created_at = models.DateTimeField(default=datetime.now())
    updated_at = models.DateTimeField(default=datetime.now())
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Permission Api'
        verbose_name = 'Permission Api'
