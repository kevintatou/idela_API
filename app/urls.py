from django.conf.urls import url
#Defining controllers being used
from app.controllers import GetController, PostController

urlpatterns = [
    #Get URL(s)
    url(r'^get/(?P<catch_all>.*)$', GetController.Get, name='Get'),
    #Post URL(s)
    url(r'^post/$', PostController.Post, name='Post'),
]

