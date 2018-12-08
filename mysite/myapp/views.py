from django.shortcuts import render
from .models import MyUser, UserEvent, Event
from django.http import HttpResponse


def handler(request, event_id):
    if request.method == 'POST':
        email = request.POST['email']
        age = request.POST['age']
        phone_number = request.POST['phone_number']
        name = request.POST['name']
        gender = request.POST['gender']
        myUser = MyUser.objects.create(name=name, age=age, email=email, phone_number=phone_number, gender=gender)
        myUserEvent = UserEvent.objects.create(user=myUser, event=event_id)
    return HttpResponse("200 OK!")


def events_list(request):
    event_list = Event.objects.all()
    return render(request, 'index.html', {"event_list": event_list})
