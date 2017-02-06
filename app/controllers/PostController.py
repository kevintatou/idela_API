from django.shortcuts import HttpResponse
from app.services.conn import *
#Defining services

from app.services import PostService
import datetime
import random
from bson import ObjectId
from faker import Faker
fake = Faker()

# Post User data
def PostUser(request):
    date = datetime.datetime.utcnow()
    name = fake.name()
    text = fake.text()
    rand_100 = random.randint(1,100)


    data = {
            "date" : date,
            "weekly" : rand_100,
            "tags" : [ 
                text[1:10], 
                text[1:6],
                text[1:10],
                text[1:10]
            ],
            "desc" : text,
            "flags" : {
                "comment" : "",
                "rating" : ""
            },
            "name" : text[1:10],
            "public" : 1,
            "token" : "",
            "image" : "https://pbs.twimg.com/profile_images/536913427789144064/yCWYL_7W_400x400.jpeg",
            "media" : "",
            "views" : random.randint(1,10000),
            "users" : {
                "owner" : "5889b49cfc0e722b749e7026",
                "members" : "5889b3f4fc0e7225f4605928"
            },
            "trending" : rand_100,
            "rating" : {
                "quality_score" : rand_100,
                "opinion_score" : rand_100,
                "relevance_score" : rand_100,
                "opinion_votes" : rand_100,
                "quality_votes" : rand_100,
                "relevance_votes" : rand_100,
                
            }
    }

    PostService.InsertData(node, data)

    return HttpResponse(1)
