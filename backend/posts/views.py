from django.shortcuts import render


def set_user_session(request):
    #gnerates a session key 
    session_id = request.session.session_key
    request.session['username'] = 'berna'
    request.session['room_code'] = '1234'






# Create your views here.
