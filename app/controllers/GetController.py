#Change from using eval at a later date

import json
from django.shortcuts import HttpResponse
#from django.core import serializers
from bson.json_util import dumps, loads
from app.services.conn import *
#Defining services
from app.services import PostService, GetService

#Calls GetService to get one user in the user collection by its ObjectId
def GetById(request, collection, id):
    #return HttpResponse(dumps(GetService.GetById(eval(collection), id)))
    return HttpResponse("ok")
#Calls GetService to get all users
def GetAll(request, collection):
    return HttpResponse(dumps(GetService.GetAll(eval(collection))))

def GetRelations(request, collection, id, relationcollection):
    return HttpResponse(dumps(GetService.GetRelations(eval(collection), id, eval(relationcollection))))

# MOVE THIS TO POSTCONTROLLER
# Post User data
def PostUser(request):
    data = {
        
    }
    PostService.InsertData(user, data)
    return HttpResponse(1)

def search(request, coll = ''):
    # Gets the parameter coll from URI and turns the string to code
    collection = request.GET.get('coll')
    
    return HttpResponse(collection.find({}))
    #if (collection == "user"):
        #coll = json.loads(collection)
    #else:
    #    return HttpResponse("rip")
