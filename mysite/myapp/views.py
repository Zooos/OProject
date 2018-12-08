from django.shortcuts import render
from .models import MyUser, UserEvent, Event
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
    # cur_date =
    # event_list = Event.objects.filter(date_start__lte=datetime.date.today())
    event_list = Event.objects.all()
    return render(request, 'index.html', {"event_list": event_list})
