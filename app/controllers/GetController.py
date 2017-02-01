from django.shortcuts import HttpResponse
from bson.json_util import dumps
from app.services.conn import *
from bson import ObjectId
#Defining services
from app.services import GetService, ValidateService


#Calls GetService to get one user in the user collection by its ObjectId
def GetById(request, collection, id):
    return HttpResponse(dumps(GetService.GetById(eval(collection), id)))
    #return HttpResponse("ok")
#Calls GetService to get all users
def GetAll(request, collection):
    return HttpResponse(dumps(GetService.GetAll(eval(collection))))

def Get(request, catch_all):
    #Terms allowed to be used in URL
    allowed_terms = [
        'col', 
        'name', 
        'id', 
        'public', 
        'tags', 
        'views', 
        'trending', 
        'media', 
        'date', 
        'alias', 
        'weekly', 
        'nodes',
        'email'
    ]


    #allowed_col_value = ['user','node','tag']

    attributes = {}

    #Catches URL and converts items and values into a dict
    catch_all = dict(item.split("=") for item in catch_all.split("&"))

    #1. Checks if items in URL are legal
    #2. If id exist change key and value to proper format for mongoDB use
    #3. if col exist put col value in new var
    for term in allowed_terms:
        for catch_item in catch_all:
            if catch_item == term:
                if catch_item == 'id':
                    attributes['_id'] = ObjectId(catch_all.get(catch_item))
                elif catch_item == 'col':
                    collection = catch_all.get(catch_item)
                else:
                    attributes[catch_item] = catch_all.get(catch_item)
    
    #Note: Send dict instead
    result = GetService.GetRequest(collection, attributes)

    return HttpResponse(dumps(result))