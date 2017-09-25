# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
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
    contentToReturn.append("<hr>")
    return contentToReturn

def getComments(post):
    DIR = "comments/"
    stringToReturn = []
    comments = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])
    for i in range(comments):
        with open("comments/" + str(i) + ".txt") as f:
            comment_author = ""
            comment_content = ""
            z = 0
            ignore = False;
            for line in f:
                if (z==0):
                    if (line != str(post)):
                        ignore = False;
                if (z == 1 and ignore == False):
                    comment_author = line
                if (z > 1 and ignore == False):
                    comment_content += line
                z += 1
            if (ignore==False):
                stringToReturn.append("<h6><em>" + comment_author + "</h6></em>" + comment_content + "<hr>")
    return "".join(stringToReturn)

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
            elif (line.find("{[Post Comments]}") != -1):
                page.append(getComments(post))
            else:
                page.append(line)
    return "".join(page)

def index(request):
    return HttpResponse(renderPostPage(request.GET['post']))
