from django.shortcuts import render
from .models import *
from django.http import HttpResponse
import datetime


def handler(request, event_id):
    if request.method == 'POST':
        email = request.POST['email']
        age = request.POST['age']
        phone_number = request.POST['phone_number']
        name = request.POST['name']
        gender = request.POST['gender']
        myUser = MyUser.objects.create(name=name, age=age, email=email, phone_number=phone_number, gender=gender)
        myUserEvent = UserEvent.objects.create(user=myUser, event=event_id)
        event = Event.objects.get(event_id)
        if event.seats >= 1:
            event.seats -= 1
    return HttpResponse("200 OK!")


def events_list(request):
    event_list = Event.objects.all()
    return render(request, 'index.html', {"event_list": event_list})


def handler_comments(request, event_id):
    if request.method == 'POST':
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        try:
            myUser = MyUser.objects.get(email=email, phone_number=phone_number)
        except:
            return HttpResponse("")
        myComment = Comments.objects.create(event=event_id, user=myUser)

    return HttpResponse("200 OK!")


