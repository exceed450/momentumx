# 
# File: urls.py
# Project: MomentumX
# Application: user_management
# Author: christian rustoeen <christian34@protonmail.com>
#
# All files are under git version control
# Follow PEP8 for coding style guide line

from django.urls import path, include
from . import views

app_name = "user"

urlpatterns = [
    path('/create', views.create_user, name='create_user'),
    path('/login', views.login_user, name='login_user'),
    path('/logout', views.logout_user, name='logout_user'),
    path('/profile', views.user_profile, name='user_profile'),
    path('/delete', views.delete_user, name='delete_user'),
    path('/disable', views.disable_user, name='disable_user'),
    path('/edit', views.edit_user_information, name='edit_user_information'),
    path('/edit/password', views.reset_password, name='reset_password'),
    path('/user/investment_profiles', views.user_investment_profiles, name='user_investment_profile'),
    path('/user/shared_profiles', views.user_shared_profiles, name='user_shared_profiles'),
    path('/user/shared_ieas', views.user_shared_ideas, name='user_shared_ideas'),
    path('/user/groups', views.user_groups, name='user_groups'),
    path('/user/permissions', views.user_permissions, name='user_permissions'),
    path('/user/settings', views.user_settings, name='user_settings'),
]
