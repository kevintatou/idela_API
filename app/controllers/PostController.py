from django.shortcuts import HttpResponse
from django.http import JsonResponse
from app.services.conn import *
import json
#Defining services
from app.services import PostService, ValidateService, SettingsService
import time

# Post User data
def Post(request):
    #Fetches time
    start_time = time.monotonic()
    
    ########### Tasks - To Do ###########
    #Authenticate user
    #Add to related collection - if needed

    #Decodes json and unlists it
    request = json.loads(request.body.decode("utf-8"))[0]

    db_col = request['col']

    if db_col == 'node':
        min_requirement = SettingsService.SettingsHandler('min_node_req')
        db_col_structure = SettingsService.SettingsHandler('db_collection_node')
    elif db_col == 'user':
        min_requirement = SettingsService.SettingsHandler('min_user_req')
        db_col_structure = SettingsService.SettingsHandler('db_collection_user')
    elif db_col == 'tags':
        min_requirement = SettingsService.SettingsHandler('min_tags_req')
        db_col_structure = SettingsService.SettingsHandler('db_collection_tags')

    #Check minimum requirements
    if ValidateService.ValidateMinRequire(request, min_requirement):

        #Structure the request for MongoDB
        formated_request = ValidateService.ValidateFormatPost(request, db_col_structure)
        
        #Posts to MongoDB
        PostService.PostRequest(formated_request, db_col)
    
    #Prints process duration
    print("API GetController process took:", time.monotonic() - start_time, "sec")

    return HttpResponse("None")
    
