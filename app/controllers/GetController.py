#-------------------------------------------------------------------------
#Change from using eval at a later date (use split instead?)
#-------------------------------------------------------------------------

from django.shortcuts import HttpResponse
#from django.core import serializers
from bson.json_util import dumps
from app.services.conn import *
#Defining services
from app.services import GetService

#Calls GetService to get one user in the user collection by its ObjectId
def GetById(request, collection, id):
    return HttpResponse(dumps(GetService.GetById(eval(collection), id)))

#Calls GetService to get all users
def GetAll(request, collection):
    return HttpResponse(dumps(GetService.GetAll(eval(collection))))

def GetRelations(request, collection, id, field, relationcollection):
    return HttpResponse(dumps(GetService.GetRelations(eval(collection), id, field, eval(relationcollection))))

def search(coll, term):
    return  coll + term + ""