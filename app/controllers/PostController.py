from django.shortcuts import HttpResponse
from app.services.conn import *
#Defining services
from app.services import PostService

# Post User data
def PostUser(request):
    data = {
        
    }
    PostService.InsertData(user, data)
    return HttpResponse(1)
