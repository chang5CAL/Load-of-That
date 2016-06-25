from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    #url(r'^test', views.test, name='test'),
    #url(r'^test2', views.test2, name='test2')
]
