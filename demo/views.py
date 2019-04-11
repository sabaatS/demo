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

def index(request):
        return render(request, 'demo/index.html')
