from django.shortcuts import render
import requests
import json
from allauth.socialaccount.models import SocialToken
import requests 

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
            print('name' in index)
            
            if ('name' in index and 'start_time' in index and
                'end_time'in index and 'place' in index and
                'location' in index['place'] and
                'city' in index['place']['location'] and
                'street' in index['place']['location']):
                event_info['name'] = index['name']
                event_info['start_time'] = index['start_time']
                event_info['end_time'] = index['end_time']
                event_info['place'] = dict()
                event_info['place']['state'] = index['place']['location']['state']
                event_info['place']['city'] = index['place']['location']['city']
                event_info['place']['street'] = index['place']['location']['street']
                print("Stored information in dictionary (Probably)")
        
        
        
        #print (request.GET['code'])
        #print(token[0])

            
    return render(request, 'api/test.html')

def test(request):
	print (request)
	print ('random stuff')
	token = request.GET["code"]
	print(token)
	payload = {
				'client_id': '003a3ad3-9d6a-493d-820e-6738c415f350',
				'client_secret': '8q7HUa7EcTcDBD668hPbg2t',
				'code': token,
				'redirect_uri': 'http://localhost:8000/api/test',
				'grant_type': 'authorization_code',
			  }
	r = requests.post('https://login.microsoftonline.com/common/oauth2/v2.0/token', data=payload)
	print(r.url)
	obj = r.json()
	print(obj)
	access_token = obj['access_token']
	print(access_token)

	return render(request, 'api/test.html')

def test2(request):
	return render(request, 'api/test2.html')
