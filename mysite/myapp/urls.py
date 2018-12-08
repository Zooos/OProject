from django.conf.urls import include, url

urlpatterns = [
    url(r'events/', 'myapp.views.events_list', name='events')
]