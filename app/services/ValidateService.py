from app.services import SettingsService
from bson import ObjectId
import datetime

#Validates a dictionary for mongodb query use
#IN: Simple dict
#OUT: A structured dict for MongoDB GET usage
def ValidateGetKeys(request):
    #Defining variables
    attribute = {}
    result = {}
    
    allowed_keys = SettingsService.SettingsHandler('allowed_keys')
    db_collections = SettingsService.SettingsHandler('db_collections')

    #Query to find multiple objects by ObjectIds
    #collection.find({"_id":{ "$in": [id, id]}})

    #Checks if keys are valid
    for key in allowed_keys:
        #if key in dict
        if key in request:
            #Changes values in request to int if allowed_keys says it is
            if allowed_keys.get(key) == int:
                attribute[key] = int(request.get(key))
                result['attribute'] = attribute
            else:
                #Changes id key and value to proper attributes for mongodb use
                if key == 'id':
                    attribute['_id'] = ObjectId(request.get(key))
                    result['attribute'] = attribute
                #Changes col key and puts value in it 
                elif key == 'col':
                    for collection in db_collections:
                        #Checks if collection is valid by comparison to db_collections
                        if collection == request.get(key):
                            result['collection'] = [request.get(key)]
                #Puts value in select key
                elif key == 'select':
                    result['select'] = [request.get(key)]
                else:
                    attribute[key] = request.get(key)
                    result['attribute'] = attribute
    return result

#Checks if the request meets the minimum requirements
#IN: Simple dictionary, collection
#OUT: Bool
def ValidateMinRequire(request, min_requirement):
    #Loops through the request and removes keys from min_requirement if they exist in request 
    for post_key in request:
        if post_key in min_requirement:
            min_requirement.remove(post_key)

    #Checks if the minimum requirements are met: Met if min_requirement is empty
    if not min_requirement:
        return True
    else:
        return False

#Turns the form request data into a dict for MongoDB use
#IN: Simple dictionary and structure dict to create
#OUT: A structured dict
def ValidateFormatPost(request, structure):
    for key in structure:
        #if the key in structure is dict return true
        if type(structure[key]) is dict:
            #Looks for the nested keys in the parent key
            for nested_key in structure[key]:
                #Loops through the request and adds values to the proper places
                if nested_key in request:
                    if type(structure[key][nested_key]) is list:
                        structure[key][nested_key] = request[nested_key].split(" ")
                    elif type(structure[key][nested_key]) == str:
                        structure[key][nested_key] = str(request[nested_key])
                    elif type(structure[key][nested_key]) == int:
                        structure[key][nested_key] = int(request[nested_key])
        else:
            #Loops through the request and adds values to the proper places
            if key in request:
                if type(structure[key]) == str:
                    structure[key] = str(request[key])
                elif type(structure[key]) == int:
                    structure[key] = int(request[key])
                elif type(structure[key]) is list:
                    structure[key] = request[key].split(" ")

    return structure
    
def ValidateExistInDB(request, col):
    
    #if db.mycollection.find({'UserIDS': { "$in": newID}}).count() > 0.
    return request