from django.shortcuts import HttpResponse
from bson import ObjectId

#
#args[0]: Collection to look in

#Gets one object by ObjectId
def GetOneById(*args):
    return args[0].find({"_id": ObjectId(args[1])})

#Gets objects related to the objected used when calling function
def GetRelation(*args):
    return 

#Gets all objects in collection
def GetAll(*args):
    return args[0].find()
