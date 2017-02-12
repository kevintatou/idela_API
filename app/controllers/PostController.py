from django.shortcuts import HttpResponse
from app.services.conn import *
#Defining services
from app.services import PostService
import datetime
import random
from faker import Faker
fake = Faker()



# Post User data
def Post(request):
    date = datetime.datetime.utcnow()


    data = {
            "date" : date,
            "weekly" : random.randint(1,100),
            "tags" : [ 
                'koda',
                'facebook',
                'live'
            ],
            "desc" : "Följ Liam i hans maniska kodsession live via Facebook's API",
            "flags" : {
                "comment" : "",
                "rating" : ""
            },
            "name" : 'Liam kodar',
            "public" : 1,
            "token" : "",
            "image" : "http://www.annatroberg.se/wp-content/uploads/2014/02/iStock_000016095582Small-1508x706_c.jpg",
            "media" : "",
            "views" : random.randint(1,10000),
            "users" : {
                "owner" : "5889b49cfc0e722b749e7026",
                "members" : "5889b3f4fc0e7225f4605928"
            },
            "trending" : random.randint(1,100),
            "rating" : {
                "quality_score" : random.randint(1,100),
                "opinion_score" : random.randint(1,100),
                "relevance_score" : random.randint(1,100),
                "opinion_votes" : random.randint(1,100),
                "quality_votes" : random.randint(1,100),
                "relevance_votes" : random.randint(1,100),
            }
    }


    return HttpResponse(PostService.InsertData(node, data))
    
'''
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
'''
