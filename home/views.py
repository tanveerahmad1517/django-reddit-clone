# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def renderPage():
    return "<form action=\"/forum\"><input type=\"text\" name=\"sub\"><input type=\"submit\"></form>"

def index(request):
    return HttpResponse(renderPage())
