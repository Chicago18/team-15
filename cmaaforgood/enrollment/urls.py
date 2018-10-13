from django.conf.urls import url, include 
from . import views

urlpatterns = [
    url('', views.index, name='index'),
    url(r'^login/$', views.login, name='login'),
    url(r'^profile/(?P<username>\w+)/$', views.profile, name='profile'),
    url(r'^parentHome/$', views.parentHome, name='parentHome'),
    url(r'^parentLogin/$', views.parentLogin, name='parentLogin'),
    url(r'^childProfile/$', views.childProfile, name='profile'),
    url(r'^forms/$', views.forms, name='forms'),
    url(r'^enroll/$', views.enroll, name='enroll'),
    ]
