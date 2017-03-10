from django.shortcuts import HttpResponse
from django.http import JsonResponse
from app.services.conn import *
import json
#Defining services
from app.services import PostService, ValidateService
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

    #Puts collection in a variable
    db_col = request['col']

    #Check minimum requirements
    if ValidateService.ValidateMinRequire(request, db_col):

        #Structure the request for MongoDB
        formated_request = ValidateService.ValidateFormatPost(request, db_col)
        
        #Posts to MongoDB
        PostService.PostRequest(formated_request, db_col)
    
    #Prints process duration
    print("API GetController process took:", time.monotonic() - start_time, "sec")

    return HttpResponse("None")
    
