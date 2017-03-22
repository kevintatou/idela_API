from app.services import SettingsService, GetService, PostService, UpdateService
from bson import ObjectId
from copy import copy
import datetime

############# TO DO #############
#Figure out something better

#Validates a dictionary for mongodb query use
#IN: Simple dict
#OUT: A structured dict for MongoDB GET use
def ValidateGetKeys(request):
    #Defining variables
    attribute = {}
    result = {}

    allowed_keys = SettingsService.SettingsHandler('allowed_keys')
    db_collections = SettingsService.SettingsHandler('db_collections')

    #######Query to find multiple objects by ObjectIds
    #######collection.find({"_id":{ "$in": [id, id]}})
    
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
    
    #Checks if min_requirement keys exist in request, If not return False
    for key in min_requirement:
        if key not in request: 
            return False
    
    return True

############# TO DO #############
#Move to FormatService

#Turns a simple dict to a sturctured one
#IN: Simple dictionary to structure and a structured dict as a guide
#OUT: A structured dict
def FormatDict(request, structure):
    for key in structure:
        #If the structure key is a dict call this function with the embedded structure keys
        if type(structure[key]) is dict:
            FormatDict(request,structure[key])
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

############# TO DO #############
#Move to a better location
def ValidateDBRelation(request, db_col):
    get_request = {}
    post_list = []

    #If a node document was created before make the relations
    if db_col == 'node':
        #Auth Users
        #Add owner and members

        #Adds a col key with value tag
        get_request['col'] = 'tag'

        #Gets the structure guide needed for MongoDB post use
        db_col_structure = SettingsService.SettingsHandler('db_collection_tags')

        #Loop through all the node tags
        for tag_name in request['tags']:
            get_request['name'] = tag_name
            
            #Validate and format for get request use
            get_result = ValidateGetKeys(get_request)
            
            #Makes a get request for a tag 
            get_result = GetService.GetRequest(get_result)

            #Format request for MongoDB use
            formated_request = FormatDict(get_request, db_col_structure)
            
            #If no document(tag) was found, append the tag to post_list
            if get_result.count() == 0:
                #Takes the ObjectId from request and turns into a string
                formated_request['nodes'] = [str(request['_id'])]
                
                #Appends a copy of formated_request
                post_list.append(copy(formated_request))
            #If document(tag) was found, update the related nodes in the tag document
            elif get_result.count() != 0:
                push_dict = {'nodes': str(request['_id'])}
                #Update the existing tags
                UpdateService.UpdateRequest(get_request['col'], get_result, push_dict)
        
        #If post_list has any items make a post request
        if len(post_list) > 0:
            #Posts many(or single) documents to MongoDB
            PostService.PostRequestMany(post_list, get_request['col'])