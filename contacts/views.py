# -*- coding: utf-8 -*-
#from __future__ import unicode_literals

from django.shortcuts import render
from django.db.models import Q
from django.http import HttpResponse
from .models import Contact

# Create your views here.
def index(request):
    #return HttpResponse('hello world')

    contacts = Contact.objects.all()[:10]
    query = request.GET.get("q")
    if query:
        contacts = Contact.objects.filter(
            Q(Name__icontains=query) |
            Q(Department__icontains=query)
            )
    #contacts = Contact.objects.filter(Name__icontains="")
    context = {
        'contacts':contacts
    }
    return render(request, 'index.html', context)

def details(request, id):
    contact = Contact.objects.get(id=id)
    context = {
        'contact':contact
    }
    return render(request, 'details.html', context)
