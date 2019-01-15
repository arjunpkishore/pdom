# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Request_Targets, Access_Requests, Permission_Api

admin.site.register(Request_Targets)
admin.site.register(Access_Requests)
admin.site.register(Permission_Api)
# Register your models here.
