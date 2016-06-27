from django.shortcuts import render
from django.template import Context, Template
from django.http import HttpResponseRedirect
import requests
import json
from allauth.socialaccount.models import SocialToken
from allauth.socialaccount.models import SocialAppManager
from datetime import datetime
import requests
from django.db import models
from rest_framework import serializers

class FacebookSerializer(serializers.ModelSerializer):
    class Meta:
        #model = 'Facebook'
        fields = ('name','start_time','place','source')

class FacebookView():
    #model = 'Facebook'
    serializer_class = FacebookSerializer
