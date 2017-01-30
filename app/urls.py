from django.conf.urls import url

#Defining controllers being used
from app.controllers import GetController

urlpatterns = [
    #Get URLs
    url(r'^get/(?P<collection>\w+)/(?P<id>\w+)/$', GetController.GetById, name='GetById'),
    url(r'^get/(?P<collection>\w+)/$', GetController.GetAll, name='GetAll'),
    url(r'^get/(?P<collection>\w+)/(?P<id>\w+)/(?P<relationcollection>\w+)/(?P<field>\w+)/$', GetController.GetRelations, name='GetRelations'),
    url(r'^get/search/coll=(?P<coll>\w+)&term=(?P<term>\w+)/$', GetController.search, name='search'),
    #Post URLs
    url(r'^post/$', GetController.PostUser, name='PostUser'),
]

#url(r'^get/coll=(?P<collection>\w+)&(?P<field>\w+)=(?P<value>\w+)&rel_coll=(?P<relationcollection>\w+)&rel_coll_field=(?P<relationfield>\w+)/$