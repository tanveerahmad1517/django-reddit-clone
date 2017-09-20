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
    print len([name for name in os.listdir('content/') if os.path.isfile(name)])
    return "Another function to add stuff to later"

def renderPage(pagetype, ):
    if(pagetype == "forum"):
        array = loadPageTemplate("forum")
        for i in range(len(array)):
            if (array[i] == "{[Posts]}"):
                populateForum()
                array[i] = "STUFF"
            return "".join(array)

def loadPageTemplate(pagetype):
    template = []
    with open("pages/" + pagetype + ".html") as f:
        for line in f:
            template.append(line)
    return template

def index(request):
    return HttpResponse(markdown2.markdown(renderPage("forum")))

