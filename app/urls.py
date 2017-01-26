from django.conf.urls import url

#Defining controllers being used
from app.controllers import GetController

urlpatterns = [
    #User URLs
    url(r'^post/$', UserController.PostUser, name='PostUser'),
    url(r'^get/(?P<collection>\w+)/(?P<id>\w+)/$', UserController.GetById, name='GetUser'),
    url(r'^get/(?P<collection>\w+)/$', UserController.GetAll, name='GetAllUsers'),
    url(r'^get/(?P<collection>\w+)/(?P<id>\w+)/(?P<relationcollection>\w+)/$', UserController.GetRelations, name='GetUserNodeRelations'),
]