from app.services import GetService, SettingsService, PostService, UpdateService, ValidateService, FormatService
from copy import copy

def DBRelation(request, db_col):
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
            #get_result = ValidateService.ValidateGetKeys(get_request)
            
            #Makes a get request for a tag 
            get_result = GetService.GetRequest(get_request)

            #Format request for MongoDB use
            formated_request = FormatService.FormatDict(get_request, db_col_structure)
            
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