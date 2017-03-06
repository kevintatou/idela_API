from django.shortcuts import HttpResponse
from bson.json_util import dumps
from app.services.conn import *
#Defining services
from app.services import GetService, ValidateService
import time

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
