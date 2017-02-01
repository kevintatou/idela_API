from django.shortcuts import HttpResponse
from bson.json_util import dumps
from app.services.conn import *
#Defining services
from app.services import GetService, ValidateService

def Get(request, catch_all):
    #Catches URL and converts items and values into a dict
    catch_all = dict(item.split("=") for item in catch_all.split("&"))
    
    #Validate for mongodb query use
    dict1 = ValidateService.ValidateGetTerms(catch_all)

    #Makes a get request
    result = GetService.GetRequest(dict1)
    
    return HttpResponse(dumps(result))