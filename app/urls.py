from django.conf.urls import url

from app.controllers import UserController

urlpatterns = [
    url(r'^get/$', UserController.index, name='index'),
    url(r'^post/$', UserController.PostUser, name='PostUser'),
]