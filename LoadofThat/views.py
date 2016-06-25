from django.shortcuts import render
from django.template import Context, Template
from datetime import datetime, timedelta

def index(request):
    # template = loader.get_template('templates/test.html')   
    obj = {
            'is_authenticated': False,
            'has_calendar': False,
            'access_token': "",
            'email_type': "",
          }
    if (request.user.is_authenticated()):
        obj['is_authenticated'] = True

    if (request.session.get('time')):
        time = request.session['time']
        dt = datetime.strptime(time[:-7], "%Y-%m-%d %H:%M:%S")
        print (time)
        print (dt)
        dt = dt + timedelta(hours=1)

        print (dt)
        if (datetime.now() > dt):
            # past 1 hour, the access token as expired, thus we delete it
            del request.session['time']
            del request.session['access_token']
        else:
            # user has a calendar and is still authenticated
            obj['has_calendar'] = True
            obj['access_token'] = request.session['access_token']
            obj['email_type'] = request.session['email_type']

    context = Context(obj)
    return render(request, 'index.html', context)
