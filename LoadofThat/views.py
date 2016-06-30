from django.shortcuts import render
from django.template import Context, Template
from datetime import datetime, timedelta

def index(request):
    # template = loader.get_template('templates/test.html')   
    obj = {
            'is_authenticated': False,
            'has_calendar': False,
            'outlook_access_token': "",
            'email_type': "",
            'eventbrite_access_token': "",
          }
    if (request.user.is_authenticated()):
        obj['is_authenticated'] = True

    check_state(request, obj, "outlook")
    check_state(request, obj, "eventbrite")

    context = Context(obj)
    print (obj)
    return render(request, 'index.html', context)

# Finds if the given session is expired
def check_state(request, obj, site):
    if (request.session.get(site + '_time')):
        time = request.session[site + '_time']
        dt = datetime.strptime(time[:-7], "%Y-%m-%d %H:%M:%S")
        print (time)
        print (dt)
        dt = dt + timedelta(hours=1)

        print (dt)
        if (datetime.now() > dt):
            # past 1 hour, the access token as expired, thus we delete it
            del request.session[site + '_time']
            del request.session[site + '_access_token']
        else:
            # user has a calendar and is still authenticated
            obj[site + '_access_token'] = request.session[site + '_access_token']
            if (site == "outlook"):
                obj['has_calendar'] = True
                obj['email_type'] = request.session['email_type']
