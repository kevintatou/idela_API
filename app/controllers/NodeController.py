from django.shortcuts import HttpResponse
from app.services import GetService
from bson.json_util import dumps
from app.services.conn import *

#Get all projects
def GetNode(request):
    return HttpResponse(dumps(GetService.GetOne(node)))
