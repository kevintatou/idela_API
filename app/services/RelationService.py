from app.services import GetService, SettingsService, PostService, UpdateService, ValidateService, FormatService
from copy import copy

def DBRelation(request, db_col):
    #If a node document was created before make the relations
    if db_col == 'node':
        #Auth Users
        #Add owner and member

        node_id = str(request['_id'])

        #Gets the structure guide needed for MongoDB post use
        db_col_structure = SettingsService.SettingsHandler('db_collection_tag')
        allowed_get_keys = SettingsService.SettingsHandler("allowed_get_keys")

        #Adds '$in' where needed
        tags = FormatService.Inify({'name': request['tags']})
        
        #Gets the existing tags in MongoDB
        get_result = GetService.GetRequest('tag', tags, None)

        #Update the existing tags
        for document in get_result:
            if document['name'] in tags['name']['$in']:
                #Updates the tag in tags collection by id 
                UpdateService.UpdateRequest('tag', document['_id'], {'nodes': node_id})
                #Removes the tag from tags list
                tags['name']['$in'].remove(document['name'])
        
        #Create a new tag document and post to tag collection
        if len(tags['name']['$in']) > 0:
            tmp_list = {}
            post_list = []

            #Format request for MongoDB use
            for tag in tags['name']['$in']:
                tmp_list['name'] = tag
                tmp_list['nodes'] = node_id

                #Format for MongoDB use
                formated_request = FormatService.FormatDict(tmp_list, db_col_structure, True)

                #Makes a copy of formated_request and appends to post_list
                post_list.append(copy(formated_request))
            
            #Posts many(or single) documents to MongoDB
            PostService.PostRequestMany(post_list, 'tag')