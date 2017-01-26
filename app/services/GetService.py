from bson import ObjectId

#How args are used
#args[0]: Collection to search in
#args[1]: ObjectId
#args[2]: Relation Collection to search in 

#Gets one object by its ObjectId
def GetById(*args):
    #Add validation
    result = args[0].find({"_id": ObjectId(args[1])})
    return result

def GetRelations(*args):
    result = args[0].find({"_id": ObjectId(args[1])},{"nodes":1})
    result = args[2].find({"_id":{"$in":result["node"]}})
    return result

#Gets all objects in collection
def GetAll(*args):
    #Add validation
    result = args[0].find()
    return result
