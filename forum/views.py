# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

#Necessary Imports
import markdown2
import os, os.path

#Create the view

def renderPost():
    return "I'll add stuff here later"

def populateForum():
    DIR = 'content/'
    stringToReturn = []
    print(len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))]))
    for i in range(len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])):
        if (i > 25):
            break;
        print(i)
        author = ""
        title = ""
        content = ""
        z = 0
        with open("content/" + str(i) + ".txt") as f:
            for line in f:
                if (z == 0):
                    title = line
                elif (z == 1):
                    author = line
                else:
                    content += line
                z += 1
            stringToReturn.append("<a href=\"post/?post=" + str(i) + "\">")
            stringToReturn.append("<b>"+title+"</a></b>"+"<br />"+"<em>"+author+"</em>"+"<h6>")
            if (len(content) > 252):
                stringToReturn.append(content[:252] + "...")
            else:
                stringToReturn.append(content)
            stringToReturn.append("</h6><hr>")
    
    return "".join(stringToReturn)

def renderPage(pagetype):
    if(pagetype == "forum"):
        array = loadPageTemplate("forum")
        for i in range(len(array)):
            print(array[i])
            if (array[i].find("{[Posts]}") != -1):
                array[i] = populateForum()
        return "".join(array)

def loadPageTemplate(pagetype):
    template = []
    with open("pages/" + pagetype + ".html") as f:
        for line in f:
            template.append(line)
    return template

def index(request):
    return HttpResponse(markdown2.markdown(renderPage("forum")))


