from django.shortcuts import HttpResponse
from bson.json_util import dumps
from app.services.conn import *
#Defining services
from app.services import GetService, ValidateService
import time

############# TO DO #############
#collection?name=hello&tags=game,computer
#Split ? and move to new var
#Split & (makes the keys)
#Split = (key, values)
#Split , into list and add "$in" as key to list - {"_id":{ "$in": value_list}}

def Get(request, catch_all):
    #Fetches time
    start_time = time.monotonic()

    #Catches URL and converts keys and values into a dict
    catch_all = dict(key.split("=") for key in catch_all.split("&"))
    
    #Validate for mongodb query use
    dict1 = ValidateService.ValidateGetKeys(catch_all)
    
    #Makes a get request
    result = GetService.GetRequest(dict1)

    #Prints process duration
    print("API GetController process took:", time.monotonic() - start_time, "sec")

    return HttpResponse(dumps(result))
