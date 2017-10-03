# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
from django.shortcuts import render
from django.http import HttpResponse

from markdown2 import *

# Create your views here.

def getPostContent(post, request):
    contentToReturn = []
    author = ""
    title = ""
    content = ""
    z = 0
    with open("content/" + str(request.GET['sub']) + "/" + str(post) + "/content.txt") as f:
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
    contentToReturn.append("<hr>")
    return contentToReturn

def getComments(post, request):
    DIR = "content/" + request.GET['sub'] + "/" + str(post) + "/comments/"
    stringToReturn = []
    comments = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])
    for i in range(comments):
        with open(DIR + str(i) + ".txt") as f:
            comment_author = ""
            comment_content = ""
            z = 0
            for line in f:
                if (z == 0):
                    comment_author = line
                else:
                    comment_content = comment_content + line
                z += 1
            stringToReturn.append("<h6><em>" + comment_author + "</h6></em>" + comment_content + "<hr>")
            z = 0
    return "".join(stringToReturn)

def renderPostPage(post, request):
    content = getPostContent(post, request)
    page = []
    with open("pages/post.html") as f:
        for line in f:
            if (line.find("{[Post title]}") != -1):
                page.append(content[0])
            elif (line.find("{[Post Author]}") != -1):
                page.append(content[1])
            elif (line.find("{[Post Content]}") != -1):
                page.append(content[2])
            elif (line.find("{[Post Comments]}") != -1):
                page.append(getComments(post, request))
            elif (line.find("{[Post ID]}") != -1):
                page.append(line.replace("{[Post ID]}",str(post)))
            elif (line.find("{[Post SUB]}") != -1):
                page.append(line.replace("{[Post SUB]}",request.GET['sub']))
            else:
                page.append(line)
    return "".join(page)

def index(request):
    return HttpResponse(renderPostPage(request.GET['post'], request))
