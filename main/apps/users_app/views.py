# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect,HttpResponse
def register(request):
    response='placeholder for users to create a new user record'
    return HttpResponse(response)
def login(request):
    response='placeholder for users to login'
    return HttpResponse(response)
def new(request):
    response='placeholder to display a new form to create a new blog'
    return HttpResponse(response)
def users(request):
    response='placeholder to later display all the list of users'
    return HttpResponse(response)
# Create your views here.
