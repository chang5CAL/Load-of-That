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
        print("They're the same! \n \n READ THIS \n \n")

        print(str(obj['data'][0]['name']) == 'Portland Children’s Museum - Superhero Day')

        for index in obj:
            if (obj['name'] and obj['start_time'] and obj['end_time'] and
                obj['place'] and obj['place']['location']['state'] and
                obj['place']['location']['city'] and
                obj['place']['location']['street']):
                #I don't know how exactly to check if they exist...
                event_info['name'] = obj['name']
                event_info['start_time'] = obj['start_time']
                event_info['end_time'] = obj['end_time']
                event_info['place'] = dict()
                event_info['place']['state'] = obj['place']['location']['state']
                event_info['place']['city'] = obj['place']['location']['city']
                event_info['place']['street'] = obj['place']['location']['street']
        
        
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