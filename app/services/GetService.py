from bson import ObjectId
import re

#How args are used
#args[0]: Collection to search in
#args[1]: ObjectId
#args[2]: Relation Collection to search in 
#args[3]: Field to get

#Gets one object by its ObjectId
def GetById(*args):
    #Add validation
    result = args[0].find({"_id": ObjectId(args[1])})
    return result

def GetRelations(*args):
    value_list = []

    query = args[0].find({"_id": ObjectId(args[1])}).distinct(args[3])

    #converts ObjectId numbers to real ObjectIds
    for value in query:
        converted_value = ObjectId(value)
        value_list.append(converted_value)
    
    result = args[2].find({"_id":{ "$in": value_list}})
        
    return result

#Gets all objects in collection
def GetAll(*args):
    #Add validation
    result = args[0].find()
    return result
