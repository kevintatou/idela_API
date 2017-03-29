from django.shortcuts import HttpResponse
from bson.json_util import dumps
from app.services.conn import *
#Defining services
from app.services import GetService, ValidateService, SettingsService, FormatService
import time

def Get(request, url_catch):
    #Fetches time
    start_time = time.monotonic()

    #Gets variables from SettingsService
    db_collections = SettingsService.SettingsHandler("db_collections")
    allowed_get_keys = SettingsService.SettingsHandler("allowed_get_keys")

    #Catches URL and converts keys and values into a dict
    url_catch = dict(key.split("=") for key in url_catch.split("&"))

    #Checks if collection is legit
    for item in db_collections:
        if item in url_catch["col"]:
            col = item
    #Removes col key from url_catch
    del url_catch["col"]

    if col == 'node':
        col_structure = SettingsService.SettingsHandler("db_collection_node")
    elif col == 'tag':
        col_structure = SettingsService.SettingsHandler("db_collection_tag")
    elif col == 'user':
        col_structure = SettingsService.SettingsHandler("db_collection_user")

    #Checks if select is used
    if "select" in url_catch:
        select = url_catch['select']
        #removes select from url_catch
        del url_catch["select"]
    else:
        select = None

    if 'id' in url_catch:
        url_catch['_id'] = url_catch['id']
        del url_catch['id']

    url_catch = FormatService.FormatDict(url_catch, col_structure, True)
    
    url_catch = FormatService.Inify(url_catch)

    url_catch = FormatService.Objectify(url_catch)

    url_catch = FormatService.MergeParentChildKeys(url_catch)

    url_catch = GetService.GetRequest(col, url_catch, select)

    #Prints process duration
    print("API GetController process took:", time.monotonic() - start_time, "sec")

    return HttpResponse(dumps(url_catch))
