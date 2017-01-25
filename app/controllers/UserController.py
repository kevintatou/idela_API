from django.shortcuts import HttpResponse
from django.core import serializers
from app.services import GetService
from bson.json_util import dumps

#Get all projects
def index(request):
    return HttpResponse(dumps(GetService.GetOne()))
