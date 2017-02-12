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
    
