from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /watercooler/
    url(r'^$', views.index, name='index'),
    # ex: /watercooler/5/
    url(r'^(?P<thread_id>[0-9]+)/$', views.thread, name='thread'),
]
