from django.conf.urls import url

from app.controllers import UserController

urlpatterns = [
    url(r'^post/$', UserController.PostUser, name='PostUser'),
    url(r'^user/(?P<user_id>\w+)/$', UserController.GetUser, name='GetUser'),
    url(r'^user/$', UserController.GetAllUsers, name='GetAllUsers'),
]