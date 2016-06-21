from django.shortcuts import render
from allauth.socialaccount.models import SocialToken
from allauth.socialaccount.models import SocialAppManager

def index(request):
    # template = loader.get_template('templates/test.html')
    token = SocialToken.objects.filter(account__user=request.user, account__provider='facebook')
    if request.method == "POST":
    	print("post")
    elif request.method == "GET":
    	print("get")
    #print (request.GET['code'])
    print(token[0])
    return render(request, 'api/test.html')