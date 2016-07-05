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
from time import localtime

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
				#event_info['start_time'] = index['start_time']
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
	print(obj['results'][0]['time'])
	print(localtime(obj['results'][0]['time']/1000))

	for index in obj['results']:	
			#print(localtime(index['time']))
			#print(index)
			if('venue' in index and 
				'state' in index['venue']):
				event_time_struct = localtime(index['time']/1000)
				#Meetup gives time in milliseconds from epoch, so it needs to be 
				#divided by 1000 so it's in seconds.

				#These if statements parse through event_time_struct and put it in
				#"%Y-%m-%dT%H:%M:%S" form. It also adds a 0 if the month or day are
				#single digit.
				if(event_time_struct.tm_mon < 10 and event_time_struct.tm_mday < 10):
					#If both month and day are single digit
					event_time_year_form = (str(event_time_struct.tm_year)+"-0"+
						str(event_time_struct.tm_mon)+"-0"+str(event_time_struct.tm_mday)+"T"+
						str(event_time_struct.tm_hour)+":"+str(event_time_struct.tm_min)+
						":"+str(event_time_struct.tm_sec))
				elif(event_time_struct.tm_mon >= 10 and event_time_struct.tm_mday < 10):
					#If only the day is single digited
					event_time_year_form = (str(event_time_struct.tm_year)+"-"+
						str(event_time_struct.tm_mon)+"-0"+str(event_time_struct.tm_mday)+"T"+
						str(event_time_struct.tm_hour)+":"+str(event_time_struct.tm_min)+
						":"+str(event_time_struct.tm_sec))
				elif(event_time_struct.tm_mon < 10 and event_time_struct.tm_mday >= 10):
					#If only the month is single digited
					event_time_year_form = (str(event_time_struct.tm_year)+"-0"+
						str(event_time_struct.tm_mon)+"-"+str(event_time_struct.tm_mday)+"T"+
						str(event_time_struct.tm_hour)+":"+str(event_time_struct.tm_min)+
						":"+str(event_time_struct.tm_sec))
				elif(event_time_struct.tm_mon >= 10 and event_time_struct.tm_mday >= 10):
					#If neither the month nor the day is single digited.
					event_time_year_form = (str(event_time_struct.tm_year)+"-"+
						str(event_time_struct.tm_mon)+"-"+str(event_time_struct.tm_mday)+"T"+
						str(event_time_struct.tm_hour)+":"+str(event_time_struct.tm_min)+
						":"+str(event_time_struct.tm_sec))
				#Note for later: The hour might need a 0 too, but it's not causing a problem yet.
				
				event_time_object = datetime.strptime(event_time_year_form, "%Y-%m-%dT%H:%M:%S")
				#print(index['title'])
				#print(index['description'])
				event_info['name'] = index['name']
				event_info['description'] = index['description']
				event_info['place'] = dict()
				event_info['start_time'] = event_time_object
				#print(index['venue'].keys())
				event_info['place']['state'] = index['venue']['state']
				event_info['place']['city'] = index['venue']['city']
				event_info['place']['street'] = index['venue']['address_1']
				event_info['source'] = 'Meetup'
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
	event_info = dict()
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
			#print (r.content)
			obj = r.json()
			print(obj['events'][0].keys())
			print(obj['events'][0]['venue_id'])
			for index in obj['events']:
				v_payload = {
					'venue_get' : index['venue_id'],
					'app_key' : 'BVSGCXUYLLFDSPVC5H',
				}
				v = requests.get('https://www.eventbrite.com/json/venue_get', params=v_payload)
				print(v)
				v_obj = v.json()
				print(v_obj)
				#I don't know what the index is for this.
				event_info['name'] = index['name']
				event_info['description'] = index['description']
				event_info['start_time'] = datetime.strptime(index['start']['utc'], "%Y-%m-%dT%H:%M:%SZ")
				event_info['place'] = dict()
				#Place is probably something about venue, but I don't know
				#what specifically.
				"""event_info['place']['state'] = index['venue']['state']
				event_info['place']['city'] = index['venue']['city']
				event_info['place']['street'] = index['venue']['address_1']"""
				event_info['source'] = 'Eventbrite'
		else:
			print("deleted sad face")
			# access token gone, delete it
			del request.session['eventbrite_time']
			del request.session['eventbrite_access_token']

	return render(request, 'api/test.html')
