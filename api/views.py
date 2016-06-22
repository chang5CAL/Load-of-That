from django.shortcuts import render
from allauth.socialaccount.models import SocialToken

def index(request):
    # template = loader.get_template('templates/test.html')

    # request.user gives us the access 
    token = SocialToken.objects.filter(account__user=request.user, account__provider='facebook')
    if request.method == "POST":
    	print("post")
    	HttpRequest.POST('graph.facebook.com/?ids=platform,me')
    elif request.method == "GET":
    	print("get")
    	HttpRequest.GET('graph.facebook.com/?ids=platform,me')
    #print (request.GET['code'])
    print(token[0])
    return render(request, 'api/test.html')
