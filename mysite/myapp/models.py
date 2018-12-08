from django.db import models


class Institutions(models.Model):
    description = models.TextField()


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


