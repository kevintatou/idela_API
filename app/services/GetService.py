from app.services.conn import *

    #Query to get object by ObjectId and select single field 
    #query = args[0].find({"_id": ObjectId(args[1])}).distinct(args[2])

    #Query to find multiple objects by ObjectIds
    #value_list = []
    #result = args[3].find({"_id":{ "$in": value_list}})

def GetRequest(*args):
    result = eval(args[0]).find(args[1])
    return result
