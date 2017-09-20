# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

from markdown2 import *

# Create your views here.

def getPostContent(post):
    contentToReturn = []
    author = ""
    title = ""
    content = ""
    z = 0
    with open("content/" + str(post) + ".txt") as f:
        for line in f:
            if (z == 0):
                title = line
            elif (z == 1):
                author = line
            else:
                content += line
            z += 1
    contentToReturn.append(title)
    contentToReturn.append(author)
    contentToReturn.append(content)
    return contentToReturn

def renderPostPage(post):
    content = getPostContent(post)
    page = []
    with open("pages/post.html") as f:
        for line in f:
            if (line.find("{[Post title]}") != -1):
                page.append(content[0])
            elif (line.find("{[Post Author]}") != -1):
                page.append(content[1])
            elif (line.find("{[Post Content]}") != -1):
                page.append(content[2])
            else:
                page.append(line)
    return "".join(page)
def index(request):
    return HttpResponse(renderPostPage(request.GET['post']))
