from django.shortcuts import HttpResponse
from bson.json_util import dumps
from app.services.conn import *
#Defining services
from app.services import GetService, ValidateService, SettingsService, FormatService
import time

def Get(request, url_catch):
    #Fetches time
    start_time = time.monotonic()

    #Gets variables
    db_collections = SettingsService.SettingsHandler("db_collections")
    allowed_get_keys = SettingsService.SettingsHandler("allowed_get_keys")

    #Catches URL and converts keys and values into a dict
    url_catch = dict(key.split("=") for key in url_catch.split("&"))

    #Adds possibility to get multiple documents by key values
    url_catch = FormatService.FormatMultipleGetValues(url_catch)
    
    #Checks if collection is legit
    for item in db_collections:
        if item in url_catch["col"]:
            col = item
    
    #Removes col key from url_catch
    del url_catch["col"]

    url_catch = ValidateService.ValidateLegalKeys(url_catch, allowed_get_keys)

    print("url_catch:",url_catch)

    #Validate for mongodb query use
    #dict1 = ValidateService.ValidateGetKeys(url_catch)
    
    #Makes a get request
    url_catch = GetService.GetRequest(col, url_catch)

    #Prints process duration
    print("API GetController process took:", time.monotonic() - start_time, "sec")

    return HttpResponse(dumps(url_catch))
