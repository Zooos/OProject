from django.db import models


class Institutions(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    x_coord = models.TextField()
    y_coord = models.TextField()


class Event(models.Model):
    description = models.TextField()
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()
    seats = models.IntegerField(max_length=5)
    institution = models.ForeignKey(Institutions, on_delete=models.CASCADE)


class Comments(models.Model):
    text = models.TextField()
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    institution = models.ForeignKey(Institutions, on_delete=models.CASCADE)
    user = models.ForeignKey('MyUser', on_delete=models.CASCADE)


class MyUser(models.Model):
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    name = models.CharField(max_length=20)
    gender = models.BooleanField()
    age = models.IntegerField()


class UserEvent(models.Model):
    user = models.ForeignKey(MyUser)
    event = models.ForeignKey(Event)


# class UserComment(models.Model):
#     user = models.ForeignKey(MyUser)
#     comment = models.ForeignKey(Comments)



