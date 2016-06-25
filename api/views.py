from django.shortcuts import render
from django.template import Context, Template
from django.http import HttpResponseRedirect
import requests
import json
from allauth.socialaccount.models import SocialToken
from allauth.socialaccount.models import SocialAppManager
from datetime import datetime
import requests 
from datetime import datetime


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
                event_info['start_time'] = index['start_time']
                event_info['place'] = dict()
                event_info['place']['state'] = index['place']['location']['state']
                event_info['place']['city'] = index['place']['location']['city']
                event_info['place']['street'] = index['place']['location']['street']
                
                if 'end_time'in index and 'place' in index:
                    event_info['end_time'] = index['end_time']
            """
            if ('name' in index and 'start_time' in index and
                'end_time'in index and 'place' in index and
                'location' in index['place'] and
                'city' in index['place']['location'] and
                'street' in index['place']['location']):
                print(datetime.now() < datetime.strptime(index['start_time'][:-5], "%Y-%m-%dT%H:%M:%S"))
                print(datetime.now())
                print(datetime.strptime(index['start_time'][:-5], "%Y-%m-%dT%H:%M:%S"))
                
                event_info['name'] = index['name']
                event_info['start_time'] = index['start_time']
                event_info['end_time'] = index['end_time']
                event_info['place'] = dict()
                event_info['place']['state'] = index['place']['location']['state']
                event_info['place']['city'] = index['place']['location']['city']
                event_info['place']['street'] = index['place']['location']['street']
            """
        
        
        
        #print (request.GET['code'])
        #print(token[0])

            
    return render(request, 'api/index.html')
# Redirection page for outlook to get access token
def test(request):
	# token = request.GET["code"]
	# print(token)
	# payload = {
	# 			'client_id': '003a3ad3-9d6a-493d-820e-6738c415f350',
	# 			'client_secret': '8q7HUa7EcTcDBD668hPbg2t',
	# 			'code': token,
	# 			'redirect_uri': 'http://localhost:8000/api/test',
	# 			'grant_type': 'authorization_code',
	# 		  }
	# r = requests.post('https://login.microsoftonline.com/common/oauth2/v2.0/token', data=payload)
	# obj = r.json()
	# access_token = obj['access_token']
	# print(access_token)
	# request.session['access_token'] = access_token
	# request.session['time'] = str(datetime.datetime.now())

	# print("RANDDOM SMA")
	# payload = {
	# 		'Authorization': 'Bearer ' + str(access_token),
	# 		'Accept': 'application/json;odata.metadata=minimal;odata.streaming=true',
	# 		'X-anchorMailBox': 'allieb@oauthplay.onmicrosoft.com'
	# }
	# r = requests.get('https://outlook.office.com/api/v2.0/me/mailfolders/inbox/messages?$top=10', headers=payload)
	# print("MORE RANDOM SMASH")
	# print (r.content)
	
	#return HttpResponseRedirect("/")
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
		request.session['visited'] = str(datetime.datetime.now())
		context = Context({"test": "first time"})
	
	return render(request, 'api/cookie.html', context)

# FB redirection page, to be removed
def fb(request):
	return render(request, 'api/index.html')

# used to test making outlook event api requests
def event(request):
	# payload = {
	# 			'Authorization': 'Bearer EwAQA+l3BAAUo4xeBIbHjhBxWOFekj4Xy2fhaGQAASu8dLc/QizC4SiB81OqeFZYE1kvwHmtjkJbL5XlAXCyovaK9JZDyGdBO7MscHRj9IeHjwIlfTwOeOMJH9qRYJcinLPbYXEnsPkOj/xXmKNx+RklbAViZI9RF7V5obfEzPoGcERy6jZ0/qj7Cua7YjKjoRFUAY6lVRpAVCQRi7iwED6Js/8Ve5Yj9ln+nOvWvoss5fdoo/2iv2B8vPs2AXaQcGt5Z7AVDmc/0hDcQ1MJdXytS1DIbcj6RddEKfiJ1I41h+ewx4AZOosDdD9EdepFGOE4kVWMLE4opBzAAVxjecRRVw9ti/OyMgQCCZ9d6R1ujPSfOP16Gav342CMOpsDZgAACMaDiJo3c+sl4AFdhMAs3ROmVFsAeB3ex0Joa1pvnbHw2rkA74BaJNMyI6tw4fn72T4loQ3vLXvrGK2BEGKAp/ahZKuogO8fCMtlbtiNRdlj9GrGIKHoV6HK+uJN8i06RT/zVXmv85fb1Oe5FUMH5GliX1pLGABVSxrVaf4mRqGl8HJ3wcK07oLRC/jYdU+KwvHEXSxk9yBYe1yaVCLEZxIk85EzqPFypkbyaUFNk1i1rMrD/Xpm3aJdspN7Ioq6tRLaLBzCz7lxJcVlPOqEpltct8+wP7gYB5y0N3FbHZrPwIMVczZrImG8E5Gh/Z4lgTTIGM5w/Kgh0xJf1PtjbY25RkVqFQMpdPpxV+OeIJHfNBxizYe/ac7Y9UlG9/DCUO+pHwomG4kGj+MQ33rXe9gACMzUlTpZ8fUVmLlqd4MG672rSCQQ86Szyw2uQE4D7sh4KPoyXNa/nmEXz6tGInKl/b5zUXilvZlrq9EyAieIQQJHaSwJv7yD/T6okUsM1418iyHdSutguj2g7fSwIfbZrsHh8rxEOrOTEiBGb8r+Us7qUyaeDDSfYqnvyz++sNZJPdBkxN7BGiUURi56N/yrxzboTzeh++g2198Z4GiS42vS5yBInOEXNZmKqA/9ZL9RS9iWuoRQgO0NAg==',
	# 		  }
	# r = requests.get('https://outlook.office.com/api/v2.0/me/events', headers=payload)
	# print (r.content)
	return render(request, 'api/test.html')
