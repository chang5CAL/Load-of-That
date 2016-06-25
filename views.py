from django.shortcuts import render
from django.template import Context, Template
from django.http import HttpResponseRedirect
import requests
import json
from allauth.socialaccount.models import SocialToken
import requests 
import datetime

def index(request):
    # template = loader.get_template('templates/test.html')    
    return render(request, 'index.html')
