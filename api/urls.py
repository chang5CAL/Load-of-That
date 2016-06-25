from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^test', views.test, name='test'),
    url(r'^cookie', views.cookie, name='cookie'),
    url(r'^fb', views.fb, name='fb'),
    url(r'^event', views.event, name='event')
]