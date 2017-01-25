from django.conf.urls import url

from app.controllers import UserController

urlpatterns = [
    url(r'^user/(?P<user_id>\w+)/$', UserController.GetUser, name='GetUser'),
    url(r'^user/$', UserController.GetAllUsers, name='GetAllUsers'),
]