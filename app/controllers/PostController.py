from django.shortcuts import HttpResponse
from django.http import JsonResponse
from app.services.conn import *
import json
#Defining services
from app.services import PostService, ValidateService, SettingsService, RelationService, FormatService
import time

def Post(request):
    #Fetches time
    start_time = time.monotonic()
    
    ########### Tasks - To Do ###########
    #Authenticate user

    #Defining variables
    result = str

    #Decodes json and unlists it
    request = json.loads(request.body.decode("utf-8"))[0]

    db_col = request['col']

    #Gets proper variables from SettingsService
    if db_col == 'node':
        min_requirement = SettingsService.SettingsHandler('min_req_node')
        db_col_structure = SettingsService.SettingsHandler('db_collection_node')
    elif db_col == 'user':
        min_requirement = SettingsService.SettingsHandler('min_req_user')
        db_col_structure = SettingsService.SettingsHandler('db_collection_user')
    elif db_col == 'tags':
        min_requirement = SettingsService.SettingsHandler('min_req_tags')
        db_col_structure = SettingsService.SettingsHandler('db_collection_tags')
    
    #Check minimum requirements
    if ValidateService.ValidateMinRequire(request, min_requirement):

        #Structure the request for MongoDB Post
        formated_request = FormatService.FormatDict(request, db_col_structure)
        
        #Posts to MongoDB
        posted_data = PostService.PostRequest(formated_request, db_col)
        
        if db_col == 'node':
            #Create relations
            RelationService.DBRelation(posted_data, db_col)
        
        result = "Request was sent"
    else:
        result = "Minimum requirements were not met"
    
    #Prints process duration
    print("API PostController process took:", time.monotonic() - start_time, "sec")

    return HttpResponse(result)
    
