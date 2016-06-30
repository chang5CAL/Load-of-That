from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    #url(r'^test', views.test, name='test'),
    #url(r'^test2', views.test2, name='test2')
    url(r'^test', views.test, name='test'),
    url(r'^play', views.play, name='play'),
    url(r'^cookie', views.cookie, name='cookie'),
    url(r'^fb', views.fb, name='fb'),
    url(r'^google', views.google, name='google'),
    url(r'^meetup', views.meetup, name='meetup'),
    url(r'^eventbrite_call', views.eventbrite_call, name='eventbrite_call'),
    url(r'^eventbrite', views.eventbrite, name='eventbrite'),
       
]

