# Create your views here.
# ~*~ coding: utf-8 ~*~

import os, datetime

from django.shortcuts import render, render_to_response
from django.template import Template, Context

def home(request):
	tm = datetime.datetime.now()
	context = {'ts': tm } 
	return render(request, 'home.html', context)

def listing(request, path):
	dir = "C:/Users/Ksysha"
	dir_context = os.listdir(dir + path)
	context = {'dir_name': dir + path, 'files': dir_context}
	return render_to_response('listing.html', context)

