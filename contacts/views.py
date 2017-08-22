# -*- coding: utf-8 -*-
#from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .models import contact

# Create your views here.
def index(request):
    #return HttpResponse('hello world')
    contacts = contact.objects.all()[:10]
    content = {
        'contacts':contacts
    }
    return render(request, 'index.html', content)
