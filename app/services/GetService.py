from app.services.conn import *

#Gets one object by its ObjectId
def GetById(*args):
    #Add validation
    result = args[0].find({"_id": ObjectId(args[1])})
    return result

def GetRelations(*args):
    value_list = []

    #Query to get object by ObjectId and select single field 
    query = args[0].find({"_id": ObjectId(args[1])}).distinct(args[2])

    #converts ObjectId value to real ObjectIds
    for value in query:
        converted_value = ObjectId(value)
        value_list.append(converted_value)
    
    #Query to find multiple objects by ObjectIds
    result = args[3].find({"_id":{ "$in": value_list}})
        
    return result

#Gets all objects in collection
def GetAll(*args):
    #Add validation
    result = args[0].find()
    return result

def GetRequest(*args):
    result = eval(args[0]).find(args[1])
    return result
