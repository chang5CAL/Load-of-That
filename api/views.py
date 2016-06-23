from django.shortcuts import render
import requests
from allauth.socialaccount.models import SocialToken
import requests 

def index(request):
    # template = loader.get_template('templates/test.html')
    print(request.user.is_authenticated())
    if request.user.is_authenticated():
        token = SocialToken.objects.filter(account__user=request.user, account__provider='facebook')
        print(token[0])
        json_token = {'access_token': token[0]}
        #request_string = 'https://graph.facebook.com/search?q=portland&type=event&access_token=' + str(token[0])
        r = requests.get('https://graph.facebook.com/search?q=portland&type=event',params=json_token)
        #r = requests.get(request_string)

        print(r.content)
        
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