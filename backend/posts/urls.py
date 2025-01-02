from django.contrib import admin
from django.urls import path
from .views import set_user_session

urlpatterns = [
    path('sessions/',set_user_session,name='user_session'),
]
