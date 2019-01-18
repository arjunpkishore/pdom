# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.shortcuts import redirect

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer

from .forms import Permission_Api_Form, Create_Resource_Form, Make_Request_Form

from .models import Request_Targets, Access_Requests, Permission_Api
from token_mgmt.models import Verification_Token
from faux_fim.models import f_fim
from faux_email.models import f_email
from app_logger.models import app_log

# Create your views here.
def index(request):
    #return HttpResponse('Permissions Management System')
    return render(request, 'perm_mgmt/index.html')

def req_received(request):
    return render(request, 'perm_mgmt/thanks.html', {'message': request.session['_pmessage']})

#@login_required
def add_api(request):
    #if not request.user.is_authenticated:
    #    return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    if request.method == 'POST':
        form = Permission_Api_Form(request.POST)
        if form.is_valid():
            api_entry = Permission_Api(name = form.cleaned_data['name']
                , api_endpoint = form.cleaned_data['api_endpoint']
                , api_token = form.cleaned_data['token']
                , api_headers = form.cleaned_data['headers']
                , api_body = form.cleaned_data['body']
                , created_by = request.user)
            request.session['_pmessage'] = 'Request to add API received'
            api_entry.save()
            return HttpResponseRedirect('/perm-mgmt/request-received/')
    else:
        form = Permission_Api_Form
    return render(request, 'perm_mgmt/permission_api.html', {'form':form})

#@login_required
def request_access(request):
    #if not request.user.is_authenticated:
    #    return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    if request.method == 'POST':
        form = Make_Request_Form(request.POST)
        if form.is_valid():
            request.session['_pmessage'] = 'Access Request received'
            return HttpResponseRedirect('/perm-mgmt/request-received/')
    else:
        form = Make_Request_Form
    return render(request, 'perm_mgmt/make_request.html', {'form':form})


def add_target(request):
#    if not request.user.is_authenticated:
#        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    if request.method == 'POST':
        form = Create_Resource_Form(request.POST)
        if form.is_valid():
            request.session['_pmessage'] = 'Request to add Resource received'
            return HttpResponseRedirect('/perm-mgmt/request-received/')
    else:
        form = Create_Resource_Form
    return render(request, 'perm_mgmt/add_target.html', {'form':form})


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
