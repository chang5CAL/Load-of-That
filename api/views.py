from django.shortcuts import render
from django.template import Context, Template
from django.http import HttpResponseRedirect
import requests
import json
from allauth.socialaccount.models import SocialToken
from allauth.socialaccount.models import SocialAppManager
from datetime import datetime, timedelta
import requests 
from api.models import FacebookModel
from api.serializer import FacebookSerializer
from rest_framework import generics

class FacebookList():
    queryset = FacebookModel.objects.all()
    serializer_class = FacebookSerializer
    

class FacebookDetail():
    queryset = FacebookModel.objects.all()
    serializer_class = FacebookSerializer

def index(request):
    # template = loader.get_template('templates/test.html')
    event_info = dict()
    
    print(request.user.is_authenticated())
    if request.user.is_authenticated():
        token = SocialToken.objects.filter(account__user=request.user, account__provider='facebook')
        print(token[0])
        json_token = {'access_token': token[0]}
        #request_string = 'https://graph.facebook.com/search?q=portland&type=event&access_token=' + str(token[0])
        r = requests.get('https://graph.facebook.com/search?q=portland&type=event',params=json_token)
        #r = requests.get(request_string)
        obj = json.loads(r.text)

        
        for index in obj['data']:
            if (datetime.now() < datetime.strptime(index['start_time'][:-5], "%Y-%m-%dT%H:%M:%S") and
                'location' in index['place'] and
                'city' in index['place']['location'] and
                'street' in index['place']['location']):
                
                event_info['name'] = index['name']
                event_info['description'] = index['description']
                event_info['start_time'] = index['start_time']
                event_info['place'] = dict()
                event_info['place']['state'] = index['place']['location']['state']
                event_info['place']['city'] = index['place']['location']['city']
                event_info['place']['street'] = index['place']['location']['street']
                event_info['source'] = 'Facebook'
                #event_info['image']
        
        
        
        #print (request.GET['code'])
        #print(token[0])

            
    return render(request, 'api/index.html')
# Redirection page for outlook to get access token
def test(request):
	token = request.GET["code"]
	print(token)
	payload = {
				'client_id': '003a3ad3-9d6a-493d-820e-6738c415f350',
				'client_secret': '8q7HUa7EcTcDBD668hPbg2t',
				'code': token
,				'redirect_uri': 'http://localhost:8000/api/test',
				'grant_type': 'authorization_code',
			  }
	r = requests.post('https://login.microsoftonline.com/common/oauth2/v2.0/token', data=payload)
	obj = r.json()
	access_token = obj['outlook_access_token']
	print(access_token)
	request.session['outlook_access_token'] = access_token
	request.session['outlook_time'] = str(datetime.now())
	request.session['email_type'] = "Outlook"
	
	#return HttpResponseRedirect("/")
	return render(request, 'api/play.html')

def play(request):
	return render(request, 'api/play.html')

# TODO: remove
# test to see how session works
def cookie(request):
	context = Context({})
	if request.session.get('visited'):
		last_visit_time = request.session.get('last_visit')
		print(last_visit_time)
		context = Context({'test': 'not the first time!'})
	else:
		request.session['visited'] = str(datetime.now())
		context = Context({"test": "first time"})
	
	return render(request, 'api/cookie.html', context)

# FB redirection page, to be removed
def fb(request):
	return render(request, 'api/index.html')

def google(request):
	token = request.GET["code"]
	print(token)
	payload = {
				'client_id': '1084307285600-c271knciittbj18tj02nornfvmangnoa.apps.googleusercontent.com',
				'client_secret': 'PA20WEpxInePjBW5ggZQX3n1',
				'code': token,
				'redirect_uri': 'http://localhost:8000/api/google',
				'grant_type': 'authorization_code',
			  }
	r = requests.post('https://www.googleapis.com/oauth2/v4/token', data=payload)
	obj = r.json()
	access_token = obj['access_token']
	print(access_token)
	request.session['access_token'] = access_token
	request.session['time'] = str(datetime.now())
	request.session['email_type'] = "Google_Calendar"

	return HttpResponseRedirect("/")

def meetup(request):
	header = {
		"Authorization": "Bearer " + "745135362b44194320532523f1b6321", 
	}
	body = {
		"key": "745135362b44194320532523f1b6321",
		"city": "seattle",
		"set": "true",
		"zip": "98105",
		"country": "us",
		"city": "seattle",
		"state": "wa",
		"page": 20,
	}
	event_info = dict()
	r = requests.get("https://api.meetup.com/2/open_events", params=body)
	#print(r.content)
	obj = r.json()
	print('Result keys:')
	print(obj['results'][0].keys())
	print(localtime(obj['results'][0]['time']))

	for index in obj['results']:	
            #print(index)
            if('id' in index):
                print("inserting")
                #print(index['title'])
                #print(index['description'])
                event_info['name'] = index['name']
                event_info['description'] = index['description']
                event_info['start_time'] = index['name']
                event_info['place'] = dict()
                event_info['place']['state'] = index['place']['venue']['state']
                event_info['place']['city'] = index['place']['venue']['city']
                event_info['place']['street'] = index['place']['venue']['address_1']
                event_info['source'] = 'Meetup'
            """if (datetime.now() < datetime.strptime(index['start_time'][:-5], "%Y-%m-%dT%H:%M:%S") and
                'location' in index['place'] and
                'city' in index['place']['location'] and
                'street' in index['place']['location']):
                print("Inserting!")
                event_info['name'] = index['title']
                event_info['description'] = index['description']
                event_info['start_time'] = index['start_time']
                event_info['place'] = dict()
                event_info['place']['state'] = index['place']['location']['state']
                event_info['place']['city'] = index['place']['location']['city']
                event_info['place']['street'] = index['place']['location']['street']
                event_info['source'] = 'Meetup'"""
	return render(request, 'api/test.html')

def eventbrite(request):
	token = request.GET["code"]
	print(token)
	payload = {
		'client_id': 'BVSGCXUYLLFDSPVC5H',
		'client_secret': 'XW5EU3SVRX3MHGDB3Q4OONQMVJRUVPVHLXMLACS3GCJILH3MNY',
		'code': token,
		'grant_type': 'authorization_code',
	}
	
	r = requests.post('https://www.eventbrite.com/oauth/token', data=payload)
	obj = r.json()

	print(obj)
	request.session['eventbrite_access_token'] = obj['access_token']
	request.session['eventbrite_time'] = str(datetime.now())
	return HttpResponseRedirect("/")

def eventbrite_call(request):
    print(request.session.get('eventbrite_time'))
    if (request.session.get('eventbrite_time')):
    	time = request.session['eventbrite_time']
    	dt = datetime.strptime(time[:-7], "%Y-%m-%d %H:%M:%S")
    	dt = dt + timedelta(hours=1)
    	if (datetime.now() < dt):
            # access token still alive, make the api call
            access_token = request.session['eventbrite_access_token']
            print (access_token)
            payload = {
    	    	'token': access_token,
    	    	'q': "coding",
    	    	'venue.city': "seattle",
	    	'venue.region': 'WA',
                }
            r = requests.get('https://www.eventbriteapi.com/v3/events/search/', params=payload)
            print (r.content)
    	#I don't know why, but bumping this forward one breaks the code.
    	else:
	        print("deleted sad face")
	        # access token gone, delete it
	        del request.session['eventbrite_time']
	        del request.session['eventbrite_access_token']

    return render(request, 'api/test.html')
