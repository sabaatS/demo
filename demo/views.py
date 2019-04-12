from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect 
from django.template import loader 
from django.contrib import auth
from django.contrib.auth.models import User
import re
from .models import *
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

def index(request):
        return render(request, 'demo/index.html')

def get_album(request):
    if request.method == 'GET':
        query = request.GET['query']
        print(query)
        albums = Album.objects.all().filter(album_name__contains=query).values()
        album_data = dict()

        for a in albums:
            id = a['id']
            name = a['album_name']
            singer = a['singer']
            album_data[id] = {'name': name, 'singer':singer}

        return JsonResponse(album_data)    
            