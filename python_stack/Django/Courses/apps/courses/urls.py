from django.conf.urls import url 
from . import views

urlpatterns = [

    url(r'^$', views.index),
    url(r'^courses/(?P<course_id>\d+)/destroy/$', views.destroy),
    url(r'^courses/(?P<course_id>\d+)/delete/$', views.delete),
    url(r'^courses/add/$', views.add),

]