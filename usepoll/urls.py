from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^coaches/$', views.coaches_request, name='coaches_request'),
    url(r'^events/$', views.events_request, name='events_request'),
    url(r'^gyms/$', views.gyms_request, name='gyms_request')
]