from django.shortcuts import render
import requests
import json
from allauth.socialaccount.models import SocialToken
from allauth.socialaccount.models import SocialAppManager

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

