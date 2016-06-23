from django.shortcuts import render
import requests
from allauth.socialaccount.models import SocialToken
from allauth.socialaccount.models import SocialAppManager

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

