from django.shortcuts import HttpResponse
from bson.json_util import dumps
from app.services.conn import *
#Defining services
from app.services import GetService, ValidateService
import time

#Calls GetService to get one user in the user collection by its ObjectId
def GetById(request, collection, id):
    return HttpResponse(dumps(GetService.GetById(eval(collection), id)))
    #return HttpResponse("ok")
#Calls GetService to get all users
def GetAll(request, collection):
    return HttpResponse(dumps(GetService.GetAll(eval(collection))))

def Get(request, catch_all):

    #Fetches time
    start_time = time.monotonic()

    #Catches URL and converts terms and values into a dict
    catch_all = dict(term.split("=") for term in catch_all.split("&"))
    
    #Validate for mongodb query use
    dict1 = ValidateService.ValidateGetTerms(catch_all)


    #Makes a get request
    result = GetService.GetRequest(dict1)

    #Fetches time and subtracts it with time at start
    elapsed_time = time.monotonic() - start_time
    print("API GetController process took:", elapsed_time, "sec")

    return HttpResponse(dumps(result))
