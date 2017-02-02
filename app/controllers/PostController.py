from django.shortcuts import HttpResponse
from app.services.conn import *
#Defining services
from app.services import PostService, ValidateService
import time

# Post data
def Post(request, catch_all):
    result = ""

    #Fetches time
    start_time = time.monotonic()

    #Catches URL and converts terms and values into a dict
    catch_all = dict(term.split("=") for term in catch_all.split("&"))

    #Validate for mongodb query use
    dict1 = ValidateService.ValidateGetTerms(catch_all)

    result = PostService.InsertData(dict1)

    #Fetches time and subtracts it with time at start
    elapsed_time = time.monotonic() - start_time
    print("API PostController process took:", elapsed_time, "sec")

    return HttpResponse(result)