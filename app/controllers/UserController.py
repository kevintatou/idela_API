from django.shortcuts import HttpResponse
from django.core import serializers
from app.services import PostService
from bson.json_util import dumps
from app.services.conn import *



def GetUser(request, user_id):
    return HttpResponse(dumps(GetService.GetOneById(user, user_id)))

def GetAllUsers(request):
    return HttpResponse(dumps(GetService.GetAll(user)))


# Post User data
def PostUser(request):
    data = {
        "entity" : "user",
        "data" : "lol"
    }
    PostService.InsertData(user, data)
    return HttpResponse(1)
