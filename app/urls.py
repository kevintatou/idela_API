from django.conf.urls import url

#Defining controllers being used
from app.controllers import GetController

urlpatterns = [
    #User URLs
    url(r'^post/$', GetController.PostUser, name='PostUser'),
    url(r'^get/(?P<collection>\w+)/(?P<id>\w+)/$', GetController.GetById, name='GetUser'),
    url(r'^get/(?P<collection>\w+)/$', GetController.GetAll, name='GetAllUsers'),
    url(r'^get/(?P<collection>\w+)/(?P<id>\w+)/(?P<relationcollection>\w+)/$', GetController.GetRelations, name='GetUserNodeRelations'),
    url(r'^search/(?P<coll>.+)/$', GetController.search, name='search')
]

