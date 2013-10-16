# Create your views here.
# ~*~ coding: utf-8 ~*~

import os, datetime

from django.shortcuts import render
from django.template import Template, Context

def home(request):
	tm = datetime.datetime.now()
	context = {'ts': tm } 
	return render(request, 'home.html', context)

