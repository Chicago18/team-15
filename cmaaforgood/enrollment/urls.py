from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/$', views.login, name='login'),
    path('profile/(?P<username>\w+)/$', views.profile, name='profile'),
    path('parentHome/$', views.parentHome, name='parentHome'),
    path('parentLogin/$', views.parentLogin, name='parentLogin'),
    path('childProfile/$', views.childProfile, name='profile'),
    path('forms/$', views.forms, name='forms'),
    path('enroll/$', views.enroll, name='enroll'),
    ]
