#Overall useful variables
def SettingsHandler(settings_req):
    #Allowed terms to be used for MongoDB use
    if settings_req == "allowed_get_keys":
        return {
            'col': str,
            'desc': str,
            'fname': str,
            'lname': str, 
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
            'owners': str,
            'members': str,
            'comment' : str,
            'type': str,
            'token_type': str,
            'token_value': str
        }
    #MongoDB collections
    elif settings_req == "db_collections":
        return [
            'user',
            'node',
            'tag',
            'softdelete',
            'feedback',
            'placeholder'
        ]
    #Minimum requirements for Node creation
    elif settings_req == "min_req_node":
        return [
            'tags',
            'name',
            'type',
            'public',
            'owners'
        ]
    #Minimum requirements for User creation
    elif settings_req == "min_req_user":
        return [
            'fname',
            'lname',
            'email',
            'token_type',
            'token_value'
        ]
    #Minimum requirements for Tag creation
    elif settings_req == "min_req_tags":
        return  [
            'name'
        ]
    #Minimum requirements for Placeholder creation
    elif settings_req == "min_req_placeholder":
        return  [
            'title',
            'desc'
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
            'flags': [
                {
                    'comment': '',
                    'rating': 0,
                }
            ],
            'name': '',
            'public': 0,
            'token': '',
            'image': '',
            'type': '',
            'views': 0,
            'user': {
                'owners': [
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
            'tokens': [
                {
                    'token_type': '',
                    'token_value': ''
                }
            ],
            'nodes': [
                ''
            ],
            'image': '',
            'views': 0,
            'weekly': 0,
            'trend': 0,
            'flags': [
                {
                    'level': 0,
                    'comment': ''
                }
            ],
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
    elif settings_req == "db_collection_placeholder":
        return {
            'title': '',
            'desc': '',
            'views': 0,
            'answer': [
                {
                    'type': '',
                    'answer_desc': '',
                    'votes': 0,
                    'created': 0
                }
            ],
            'created': 0
        }
    #settings_req didnt meet any of the listed variables
    else:
        return False