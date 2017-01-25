from django.shortcuts import HttpResponse
from app.services import GetService
from bson.json_util import dumps
from app.services.conn import *

def GetUser(request, user_id):
    return HttpResponse(dumps(GetService.GetOneById(user, user_id)))

def GetAllUsers(request):
    return HttpResponse(dumps(GetService.GetAll(user)))
