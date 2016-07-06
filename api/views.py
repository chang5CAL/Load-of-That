from django.shortcuts import render
from django.template import Context, Template
from django.http import HttpResponseRedirect
import requests
import json
from allauth.socialaccount.models import SocialToken
from allauth.socialaccount.models import SocialAppManager
from datetime import datetime, timedelta
import requests

# REST API Libraries
from api.models import Facebook
from api.serializer import FacebookSerializer
from rest_framework import generics
from time import localtime
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

class FacebookList():
	queryset = Facebook.objects.all()
	serializer_class = FacebookSerializer
	

class FacebookDetail():
	queryset = Facebook.objects.all()
	serializer_class = FacebookSerializer

def index(request):
	# template = loader.get_template('templates/test.html')
	event_list = []

	city = request.GET.get("city")
	state = request.GET.get("state")
	country = request.GET.get("country")
	r_type = request.GET.get("type")
	if(or city == None or state == None
		or country == None or r_type == None):
		return HttpResponse(status=404)
	idnum = 1000000

	print(request.user.is_authenticated())
	if request.user.is_authenticated():
		token = SocialToken.objects.filter(account__user=request.user, account__provider='facebook')
		print(token[0])
		body = {
			"type":event,
			"q": city+r_type,
			"access_token":token[0],
		}
		#request_string = 'https://graph.facebook.com/search?q=portland&type=event&access_token=' + str(token[0])
		r = requests.get('https://graph.facebook.com/search',params=body)
		#r = requests.get(request_string)
		obj = json.loads(r.text)

		for index in obj['data']:
			if (datetime.now() < datetime.strptime(index['start_time'][:-5], "%Y-%m-%dT%H:%M:%S") and
				'location' in index['place'] and
				'city' in index['place']['location'] and
				'street' in index['place']['location']):
				event_info = dict()
				event_info['name'] = index['name']
				event_info['description'] = (index['description'])
				#event_info['start_time'] = index['start_time']
				event_info['start_time'] = (index['start_time'])

				event_info['end_time'] = ""
				event_info['url'] = ""
				event_info['image'] = ""
				#Facebook does not include these.
				event_info['place'] = (dict())
				event_info['place']['state'] = (index['place']['location']['state'])
				event_info['place']['city'] = (index['place']['location']['city'])
				event_info['place']['street'] = (index['place']['location']['street'])
				event_info['source'] = ('Facebook')
				event_info['id'] = idnum
				idnum += 1
				event_list.append(event_info)
		
		
		
		#print (request.GET['code'])
		#print(token[0])

	#rest_get = FacebookModel(event_list)
	return JSONResponse(event_list)
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

	idnum = 2000000
	city = request.GET.get("city")
	state = request.GET.get("state")
	country = request.GET.get("country")
	r_type = request.GET.get("type")

	if(or city == None or state == None
		or country == None or r_type == None):
		return HttpResponse(status=404)
	header = {
		"Authorization": "Bearer " + "745135362b44194320532523f1b6321", 
	}
	body = {
		"key": "745135362b44194320532523f1b6321",
		#"city": "seattle",
		"set": "true",
		#"zip": "98105",
		"country": country,
		"city": city,
		"state": state,
		"page": 20,
	}
	rest_get = None
	event_list = []
	r = requests.get("https://api.meetup.com/2/open_events", params=body)
	#print(r.content)
	obj = r.json()

	for index in obj['results']:	
		#print(localtime(index['time']))
		#print(index)
		if('venue' in index and 
			'state' in index['venue'] and
			'duration' in index):
			event_time_struct = localtime(index['time']/1000)
			event_end_time_struct = localtime((index['time']+index['duration'])/1000)
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

			#This one is for the end time.
			if(event_end_time_struct.tm_mon < 10 and event_end_time_struct.tm_mday < 10):
				#If both month and day are single digit
				event_end_time_year_form = (str(event_end_time_struct.tm_year)+"-0"+
					str(event_end_time_struct.tm_mon)+"-0"+str(event_end_time_struct.tm_mday)+"T"+
					str(event_end_time_struct.tm_hour)+":"+str(event_end_time_struct.tm_min)+
					":"+str(event_end_time_struct.tm_sec))
			elif(event_end_time_struct.tm_mon >= 10 and event_end_time_struct.tm_mday < 10):
				#If only the day is single digited
				event_end_time_year_form = (str(event_end_time_struct.tm_year)+"-"+
					str(event_end_time_struct.tm_mon)+"-0"+str(event_end_time_struct.tm_mday)+"T"+
					str(event_end_time_struct.tm_hour)+":"+str(event_end_time_struct.tm_min)+
					":"+str(event_end_time_struct.tm_sec))
			elif(event_end_time_struct.tm_mon < 10 and event_end_time_struct.tm_mday >= 10):
				#If only the month is single digited
				event_end_time_year_form = (str(event_end_time_struct.tm_year)+"-0"+
					str(event_end_time_struct.tm_mon)+"-"+str(event_end_time_struct.tm_mday)+"T"+
					str(event_end_time_struct.tm_hour)+":"+str(event_end_time_struct.tm_min)+
					":"+str(event_end_time_struct.tm_sec))
			elif(event_end_time_struct.tm_mon >= 10 and event_end_time_struct.tm_mday >= 10):
				#If neither the month nor the day is single digited.
				event_end_time_year_form = (str(event_end_time_struct.tm_year)+"-"+
					str(event_end_time_struct.tm_mon)+"-"+str(event_end_time_struct.tm_mday)+"T"+
					str(event_end_time_struct.tm_hour)+":"+str(event_end_time_struct.tm_min)+
					":"+str(event_end_time_struct.tm_sec))
			#Note for later: The hour might need a 0 too, but it's not causing a problem yet.
			
			event_time_object = datetime.strptime(event_time_year_form, "%Y-%m-%dT%H:%M:%S")
			event_end_time_object = datetime.strptime(event_end_time_year_form, "%Y-%m-%dT%H:%M:%S")
		
			#print(index['title'])
			#print(index['description'])
			event_info = dict()
			event_info['name'] = index['name']
			if 'description' in index:
				event_info['description'] = index['description']
				event_info['start_time'] = event_time_object
				event_info['end_time'] = event_end_time_object
				event_info['place'] = dict()
				event_info['place']['state'] = index['venue']['state']
				event_info['place']['city'] = index['venue']['city']
				event_info['place']['street'] = index['venue']['address_1']
				event_info['url'] = index['event_url']
				if('event_hosts' in index and 'photo' in index['event_hosts']
					and 'photo_link' in index['event_hosts']['photo']):
					event_info['image'] = index["event_hosts"]['photo']['photo_link']
				else:
					event_info['image'] = ""
				event_info['source'] = 'Meetup'
				event_info['id'] = idnum
				idnum += 1
				event_list.append(event_info)
				#rest_get = Facebook(name=event_info['name'])
	#rest_get = Facebook(name='name123445435q23tet24t')
	#rest_get.save()
	#rest_get = Facebook.objects.all()
	#rest_serializer = FacebookSerializer(event_list[0])
	#print(rest_serializer.data)
	#print(Facebook.objects.all())
	return JSONResponse(event_list)


def eventbrite(request):
	token = request.GET.get("code")
	print(token)
	if(token == None""" or city == None or state == None
		or country == None or r_type == None"""):
		return HttpResponse(status=404)
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
	event_list = []
	idnum = 3000000
	city = request.GET.get("city")
	state = request.GET.get("state")
	country = request.GET.get("country")
	r_type = request.GET.get("type")
	if(or city == None or state == None
		or country == None or r_type == None):
		return HttpResponse(status=404)

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
				'q': r_type,
				'venue.city': city,
				'venue.region': state,
				'venue.country': country,
				}
			r = requests.get('https://www.eventbriteapi.com/v3/events/search/', params=payload)
			#print (r.content)
			obj = r.json()
			#print(obj['events'][0].keys())
			#print(obj['events'][0]['venue_id'])
			print(obj['events'][0].keys())
			for index in obj['events']:
				v_payload = {
					'token' : access_token,
				}
				v = requests.get('https://www.eventbriteapi.com/v3/venues/' + index['venue_id'], params=v_payload)
				#Need to request venue in order to get place information from eventbrite.
				v_obj = v.json()

				i = requests.get('https://www.eventbriteapi.com/v3/media/' + index['logo_id'], params=v_payload)
				i_obj = i.json()

				event_info = dict()
				event_info['name'] = index['name']['text']
				event_info['description'] = index['description']['text']
				event_info['start_time'] = datetime.strptime(index['start']['utc'], "%Y-%m-%dT%H:%M:%SZ")
				event_info['end_time'] = datetime.strptime(index['end']['utc'], "%Y-%m-%dT%H:%M:%SZ")
				event_info['url'] = ""
				event_info['image'] = i_obj['url']
				event_info['place'] = dict()
				event_info['place']['state'] = v_obj['address']['region']
				event_info['place']['city'] = v_obj['address']['city']
				event_info['place']['street'] = v_obj['address']['address_1']
				event_info['source'] = 'Eventbrite'
				event_info['id'] = idnum
				idnum += 1
				event_list.append(event_info)
		else:
			print("deleted sad face")
			# access token gone, delete it
			del request.session['eventbrite_time']
			del request.session['eventbrite_access_token']

	return JSONResponse(event_list)

