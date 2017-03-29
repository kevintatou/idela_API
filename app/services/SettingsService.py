#Overall useful variables
def SettingsHandler(settings_req):
    #Allowed terms to be used for MongoDB use
    if settings_req == "allowed_get_keys":
        return {
            'col': str,
            'desc': str,
            'name': str, 
            'id': str, 
            'public': int, 
            'tags': str, 
            'views': int, 
            'trend': int, 
            'media': int, 
            'date': int, 
            'alias': str, 
            'weekly': int, 
            'nodes': str,
            'email': str,
            'owner': str,
            'members': str,
            'comment' : str
        }
    #MongoDB collections
    elif settings_req == "db_collections":
        return [
            'user',
            'node',
            'tag',
            'softdelete',
            'feedback'
        ]
    #Minimum requirements for Node creation
    elif settings_req == "min_req_node":
        return [
            'tags',
            'name',
            'type',
            'public',
            'owner'
        ]
    #Minimum requirements for User creation
    elif settings_req == "min_req_user":
        return [
            'fname',
            'lname',
            'email',
            'tokens'
        ]
    #Minimum requirements for Tag creation
    elif settings_req == "min_req_tags":
        return  [
            'name'
        ]
    #MongoDB structure for Node collection
    elif settings_req == "db_collection_node":
        return {
            '_id': '',
            'created': 0,
            'updated': 0,
            'weekly': 0,
            'tags': [
                ''
            ],
            'desc': '',
            'flags': [{
                'comment': '',
                'rating': '',
            }],
            'name': '',
            'public': 0,
            'token': '',
            'image': '',
            'type': '',
            'views': 0,
            'user': {
                'owner': [
                    ''
                ],
                'members': [
                    ''
                ],
            },
            'trend': 0,
            'rating' : {
                'qua_score': 0,
                'op_score': 0,
                'rel_score': 0,
                'op_votes': 0,
                'qua_votes': 0,
                'rel_votes': 0
            }
        }
    elif settings_req == "db_collection_user":
        return {
            '_id': '',
            'alias': '',
            'fname': '',
            'lname': '',
            'email': '',
            'desc': '',
            'tokens': '',
            'nodes': [
                ''
            ],
            'image': '',
            'views': 0,
            'weekly': 0,
            'trend': 0,
            'flags': [{
                'level': 0,
                'comment': ''
            }],
            'created': 0,
            'updated': 0
        }
    elif settings_req == "db_collection_tag":
        return {
            '_id': '',
            'name': '',
            'desc': '',
            'nodes': [ 
                ''
            ],
            'created': 0,
            'updated': 0
        }
    #settings_req didnt meet any of the listed variables
    else:
        return False