from django.shortcuts import HttpResponse
from django.http import JsonResponse
from app.services.conn import *
import json
#Defining services
from app.services import PostService, ValidateService
import time


#For testing
import datetime

# Post User data
def Post(request):
    #Fetches time
    start_time = time.monotonic()
    
    ########### Tasks - To Do ###########
    #Authenticate user
    #Add to related collection - if needed
    #Post to DB

    #Decodes json and unlists it
    request = json.loads(request.body.decode("utf-8"))[0]

    #Check minimum requirements
    if ValidateService.ValidateMinRequire(request):
        #Structure the request for MongoDB
        request = ValidateService.ValidateFormatPost(request)

    #Fetches time and subtracts it with start_time
    elapsed_time = time.monotonic() - start_time
    #Prints how long the process took
    print("API PostController process took:", elapsed_time, "sec")

    return HttpResponse(request)
    
