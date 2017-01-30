from django.conf.urls import url
#Defining controllers being used
from app.controllers import GetController, PostController

urlpatterns = [
    #Get URLs
    url(r'^get/(?P<collection>\w+)/(?P<id>\w+)/$', GetController.GetById, name='GetById'),
    url(r'^get/(?P<collection>\w+)/$', GetController.GetAll, name='GetAll'),
    url(r'^get/(?P<collection>\w+)/(?P<id>\w+)/(?P<relationcollection>\w+)/(?P<field>\w+)/$', GetController.GetRelations, name='GetRelations'),
    url(r'^get/search/coll=(?P<coll>\w+)&term=(?P<term>\w+)/$', GetController.search, name='search'),
    #Post URLs
    url(r'^post/$', PostController.PostUser, name='PostUser'),
    #Test
    url(r'^test/(?P<catch_all>.*)$', GetController.Test, name='Test'),
]