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
	home_dir = "C:/Users/Ksysha/"
	dir_context = os.listdir(home_dir + path)
	file = []
	dir = []
	for d in dir_context:
		full_path = home_dir + path + "/" + d
		if (os.path.isfile(full_path)):
			file.append(d)
		elif (os.path.isdir(full_path)):
			dir.append(d)
	
	context = {'dir_name': home_dir + path, 'files': file, 'dirs': dir}
	return render_to_response('listing.html', context)

