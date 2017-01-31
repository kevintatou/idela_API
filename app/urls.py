from django.conf.urls import url
#Defining controllers being used
from app.controllers import GetController, PostController

urlpatterns = [
    #Get URLs
    url(r'^get/(?P<collection>\w+)/(?P<id>\w+)/$', GetController.GetById, name='GetById'),
    url(r'^get/(?P<collection>\w+)/$', GetController.GetAll, name='GetAll'),
    url(r'^get/(?P<collection>\w+)/(?P<id>\w+)/(?P<relationcollection>\w+)/(?P<field>\w+)/$', GetController.GetRelations, name='GetRelations'),
    #Post URLs
    url(r'^post/$', PostController.PostUser, name='PostUser'),
    #Test
    url(r'^get_test/(?P<catch_all>.*)$', GetController.Get, name='Get'),
]