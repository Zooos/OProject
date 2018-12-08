from django.contrib import admin

from .models import Institutions, Event, Comments, MyUser

# Register your models here.
admin.site.register(Institutions)
admin.site.register(Event)
admin.site.register(Comments)
admin.site.register(MyUser)