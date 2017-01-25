from django.shortcuts import HttpResponse
from django.core import serializers
from app.services import PostService
from bson.json_util import dumps
from app.services.conn import *
from django.views.decorators.csrf import csrf_exempt


#Get all projects
def index(request):
    return HttpResponse(dumps(GetService.GetOne()))


# Post User data
def PostUser(request):
    data = {
        "entity" : "user",
        "data" : "lol"
    }
    PostService.InsertData(user, data)
    return HttpResponse(1)