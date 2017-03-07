from app.services import SettingsService
from bson import ObjectId

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
#IN: Form data object
#OUT: Bool
def ValidateMinRequire(request):
    #Finds collection in request and gets the relevant minimum requirements for that collection
    #if no collection was found return False
    if request.POST.get('col') == 'node':
        min_requirement = SettingsService.SettingsHandler('min_node_req')
    elif request.POST.get('col') == 'user':
        min_requirement = SettingsService.SettingsHandler('min_user_req')
    elif request.POST.get('col') == 'tags':
        min_requirement = SettingsService.SettingsHandler('min_tags_req')
    else:
        return False

    #Loops through the request and removes keys from min_requirement if they exist in request 
    for post_key, post_value in request.POST.lists():
        for req_key in min_requirement:
            if post_key == req_key:
                min_requirement.remove(req_key)

    #Checks if the minimum requirements are met: Met if min_requirement is empty
    if not min_requirement:
        return True
    else:
        return False

#Turns the form request data into a dict for MongoDB use
#IN: Form data object
#OUT: A structured dict for MongoDB POST usage
def ValidateFormatPost(request):
    result = {}

    #Finds collection in request and gets relevant collection structure
    #if no collection was found return False
    if request.POST.get('col') == 'node':
        db_col_structure = SettingsService.SettingsHandler('db_collection_node')
    elif request.POST.get('col') == 'user':
        db_col_structure = SettingsService.SettingsHandler('db_collection_user')
    elif request.POST.get('col') == 'tags':
        db_col_structure = SettingsService.SettingsHandler('db_collection_tags')
    else:
        return False

    #db_col_structure['name'] = request.POST.get('name')

    for post_key, post_value in request.POST.lists():
        if post_key in db_col_structure:
            if db_col_structure[post_key] == str:
                db_col_structure[post_key] = str(post_value[0])
            elif db_col_structure[post_key] == int:
                db_col_structure[post_key] = int(post_value[0])
            elif type(db_col_structure[post_key]) is list:
                post_value = post_value[0].split(" ")
                db_col_structure[post_key] = list(post_value)
                print(db_col_structure[post_key])
        elif post_key in db_col_structure['users']:
            db_col_structure['users'][post_key] = post_value
            
    return result