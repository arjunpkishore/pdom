# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer
# Create your views here.
def index(request):
    #return HttpResponse('Permissions Management System')
    return render(request, 'perm_mgmt/index.html')

def add_api(request):
    return render(request, 'perm_mgmt/permission_api.html')

def request_access(request):
    return render(request, 'perm_mgmt/make_request.html')

def add_target(request):
    return render(request, 'perm_mgmt/add_target.html')

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
