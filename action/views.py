# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
from django.http import HttpResponse

from django.shortcuts import render

# Create your views here.

def createPost(request):
    print("Filler")

def createComment(request):
    postid = request.GET['post']
    content = request.GET['content']
    author = request.GET['author']
    DIR = 'comments/'
    commentID = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])
    f = open(DIR + str(commentID) + ".txt", "w+")
    f.write(postid + "\n" + author + "\n" + content + "\n")

def theDecider(request):
    if (request.GET['type'] == "comment"):
        createComment(request)
    elif (request.GET['type'] == "post"):
        createPost(request)
    else:
        print("Error: Unknown Request Type(action)")

def index(request):
    return HttpResponse(theDecider(request))
