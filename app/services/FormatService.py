from bson import ObjectId
from copy import copy

#Turns a simple dict to a sturctured one
#IN: Simple dictionary to structure and a structured dict as a guide
#OUT: A structured dict
def FormatDict(request, structure, remove_empty):
    return_structure = {}
    for key in structure:
        #If the structure key is a dict call this function with the embedded structure keys
        if type(structure[key]) is dict:
            return_structure[key] = FormatDict(request, structure[key], remove_empty)
            if remove_empty == True and return_structure[key] == {}:
                del return_structure[key]
        elif type(structure[key]) is list:
            for item in structure[key]:
                if type(item) is dict:
                    return_structure[key] = [FormatDict(request, item, remove_empty)]
                    if remove_empty == True and return_structure[key] == [{}]:
                        del return_structure[key]
                elif key in request:
                    if type(structure[key]) is list:
                        return_structure[key] = request[key].split(",")
        else:
            #Loops through the request and adds values to the proper places
            if key in request:
                if type(structure[key]) == str:
                    return_structure[key] = str(request[key])
                elif type(structure[key]) == int:
                    return_structure[key] = int(request[key])
            elif remove_empty == False:
                return_structure[key] = structure[key]
    
    return return_structure

#Adds $in to proper places in a dictionary (request)
#IN: Dict
#Out: Dict with $in where needed
def Inify(request):
    for key in request:
        if type(request[key]) is dict:
            Inify(request[key])
        elif type(request[key]) is str:
            request[key] = request[key].split(",")
            if len(request[key]) == 1:
                request[key] = request[key][0]
            elif len(request[key]) > 1:
                request[key] = {"$in" : request[key]}
        elif type(request[key]) is list and len(request[key]) > 1:
            request[key] = {"$in" : request[key]}
        elif type(request[key]) is list and len(request[key]) == 1:
            for key2 in request[key]:
                if type(key2) is dict:
                    Inify(key2)
                else:
                    request[key] = request[key][0]
        
    return request

#Makes id numbers into ObjectId(s)
#IN: Dict with _id key
#Out: Dict with ObjectId values
def Objectify(request):
    if '_id' in request:
        if '$in' in request['_id']:
            id_list = []
            for id_item in request['_id']['$in']:
                id_list.append(ObjectId(id_item))
            request['_id']['$in'] = id_list
        elif type(request['_id']) is str:
            request['_id'] = ObjectId(request['_id'])

    return request

#Merges Parent with child key name into a single key (For mongoDB)
#IN: Structured dict
#Out: Dict with merged parent and child keys except for '$in'
def MergeParentChildKeys(request):
    return_dict = copy(request)
    for key in request:
        if type(request[key]) is dict and '$in' not in request[key]:
            for nested_key in request[key]:
                merged_key = key + '.' + nested_key
                return_dict[merged_key] = request[key][nested_key]

                del return_dict[key]

    return return_dict
