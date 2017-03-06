from django.shortcuts import HttpResponse
from app.services.conn import *
import datetime
#Defining services
from app.services import PostService, ValidateService

#For testing
from bson.json_util import dumps

# Post User data
def Post(request, collection):
    #To do - Add auth 
    print(collection)

    date = datetime.datetime.utcnow()

    data = {
        "date" : date,
        "weekly" : 1,
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
        "views" : 1,
        "users" : {
            "owner" : "5889b49cfc0e722b749e7026",
            "members" : "5889b3f4fc0e7225f4605928"
        },
        "trending" : 1,
        "rating" : {
            "quality_score" : 1,
            "opinion_score" : 1,
            "relevance_score" : 1,
            "opinion_votes" : 1,
            "quality_votes" : 1,
            "relevance_votes" : 1,
        }
    }

    ValidateService.ValidatePostNodes("test")

    return HttpResponse(request)
    #return HttpResponse(PostService.InsertData(node, data))
    
