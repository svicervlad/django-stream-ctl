from django.conf.urls import url
from ctl import views


urlpatterns = [
    url(r'^$', views.Sysctl.as_view()),
    url(r'^timers_stop$', views.Sysctl.timers_stop, name='timers_stop'),
    url(r'^timers_start$', views.Sysctl.timers_start, name='timers_start'),
    url(r'^stream_start$', views.Sysctl.sream_start, name='stream_start'),
    url(r'^stream_stop$', views.Sysctl.sream_stop, name='stream_stop'),
    url(r'^ajax$', views.Sysctl.ajax, name='ajax'),
]