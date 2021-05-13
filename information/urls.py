# File: urls.py
# Project: Momentumx
# Application: Information
# Author: Christian Rustooen <christian34@protonmail.com>
#
# All files are under git version control
# Follow PEP8 for style guide

from django.urls import path
from . import views

app_name = "info"

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('help', views.help, name='help'),
    path('learn', views.learn_to_invest, name='learn_to_invest'),
]

