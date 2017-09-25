# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
from django.http import HttpResponse

from django.shortcuts import render

# Create your views here.

def createPost(request):
    content = request.GET['comment']
    author = request.GET['author']
    title = request.GET['title']
    DIR = 'content/'
    postid = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])
    f = open(DIR + str(postid) + ".txt", "w+")
    f.write(title + "\n" + author + "\n" + content)
    f.close()
    return "<head><meta http-equiv=\"refresh\" content=\"0;URL='/post/?post=" + str(postid) + "'\" /></head>"

def createComment(request):
    postid = request.GET['post']
    content = request.GET['comment']
    author = request.GET['author']
    DIR = 'comments/'
    commentID = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])
    f = open(DIR + str(commentID) + ".txt", "w+")
    f.write(postid + "\n" + author + "\n" + content + "\n")
    f.close()

def theDecider(request):
    if (request.GET['type'] == "comment"):
        createComment(request)
        return "<head><meta http-equiv=\"refresh\" content=\"0;URL='/post/?post=" + str(request.GET['post']) +  "'\" /></head>"
    elif (request.GET['type'] == "post"):
        return createPost(request)
    else:
        print("Error: Unknown Request Type(action)")

def index(request):
    return HttpResponse(theDecider(request))
