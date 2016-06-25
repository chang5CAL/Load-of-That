from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
<<<<<<< HEAD
    #url(r'^test', views.test, name='test'),
    #url(r'^test2', views.test2, name='test2')
]
=======
    url(r'^test', views.test, name='test'),
    url(r'^cookie', views.cookie, name='cookie'),
    url(r'^fb', views.fb, name='fb'),
    url(r'^event', views.event, name='event')
]
>>>>>>> 9a7b086dc28dfc4657499f3a0cc884d2c2a03b72
