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
        for request_key in request:
            if request_key == key:
                #Changes values in request to int if allowed_keys says it is
                if allowed_keys.get(key) == int:
                    attribute[request_key] = int(request.get(request_key))
                    result['attribute'] = attribute
                else:
                    #Changes id key and value to proper attributes for mongodb use
                    if request_key == 'id':
                        attribute['_id'] = ObjectId(request.get(request_key))
                        result['attribute'] = attribute
                    #Changes col key and puts value in it 
                    elif request_key == 'col':
                        for collection in db_collections:
                            #Checks if collection is valid by comparison to db_collections
                            if collection == request.get(request_key):
                                result['collection'] = [request.get(request_key)]
                    #Puts value in select key
                    elif request_key == 'select':
                        result['select'] = [request.get(request_key)]
                    else:
                        attribute[request_key] = request.get(request_key)
                        result['attribute'] = attribute

    return result

#Checks if the request meets the minimum requirements
#IN: Simple dictionary
#OUT: Bool
def ValidateMinRequire(request):
    #Finds collection in request and gets the relevant minimum requirements for that collection
    #if no collection was found return False
    if request['col'] == 'node':
        min_requirement = SettingsService.SettingsHandler('min_node_req')
    elif request['col'] == 'user':
        min_requirement = SettingsService.SettingsHandler('min_user_req')
    elif request['col'] == 'tags':
        min_requirement = SettingsService.SettingsHandler('min_tags_req')
    else:
        return False

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
#IN: Simple dictionary
#OUT: A structured dict for MongoDB POST use
def ValidateFormatPost(request):

    #Finds collection in request and gets relevant collection structure
    #if no collection was found return False
    if request['col'] == 'node':
        db_col_structure = SettingsService.SettingsHandler('db_collection_node')
    elif request['col'] == 'user':
        db_col_structure = SettingsService.SettingsHandler('user_post_keys_allowed')
    elif request['col'] == 'tags':
        db_col_structure = SettingsService.SettingsHandler('tag_post_keys_allowed')
    else:
        return False

    for col_key in db_col_structure:
        #if the key in db_col_structure is dict return true
        if type(db_col_structure[col_key]) is dict:
            #Looks for the nested keys in the parent key
            for nested_keys in db_col_structure[col_key]:
                #Loops through the request and adds values to the proper places
                for request_key in request:
                    if nested_keys == request_key:
                        if nested_keys == "members":
                            db_col_structure[col_key][nested_keys] = request[nested_keys].split(" ")
                        elif type(db_col_structure[col_key][nested_keys]) == str:
                            db_col_structure[col_key][nested_keys] = str(request[nested_keys])
                        elif type(db_col_structure[col_key][nested_keys]) == int:
                            db_col_structure[col_key][nested_keys] = int(request[nested_keys])
        else:
            #Loops through the request and adds values to the proper places
            if col_key in request:
                if type(db_col_structure[col_key]) == str:
                    db_col_structure[col_key] = str(request[col_key])
                elif type(db_col_structure[col_key]) == int:
                    db_col_structure[col_key] = int(request[col_key])
                elif type(db_col_structure[col_key]) is list:
                    db_col_structure[col_key] = request[col_key].split(" ")

    #Time stamp
    db_col_structure['date'] = datetime.datetime.utcnow()

    return db_col_structure
    