#Overall useful variables
def SettingsHandler(settings_req):
    #Allowed terms to be used for MongoDB use
    if settings_req == "allowed_keys":
        return {
            'col': str, 
            'name': str, 
            'id': str, 
            'public': int, 
            'tags': str, 
            'views': int, 
            'trending': int, 
            'media': int, 
            'date': int, 
            'alias': str, 
            'weekly': int, 
            'nodes': str,
            'select': str,
            'email': str
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
    elif settings_req == "min_node_req":
        return [
            'tags',
            'name',
            'public',
            'owner'
        ]
    #Minimum requirements for User creation
    elif settings_req == "min_user_req":
        return [
            'firstname',
            'lastname',
            'email',
            'tokens'
        ]
    #Minimum requirements for Tag creation
    elif settings_req == "min_tags_req":
        return  [
            'name'
        ]
    #MongoDB structure for Node collection
    elif settings_req == "db_collection_node":
        return {
            'created_on': 0,
            'updated_on': 0,
            'weekly': 0,
            'tags': [
                ''
            ],
            'desc': '',
            'flags': {
                'comment': '',
                'rating': '',
            },
            'name': '',
            'public': 0,
            'token': '',
            'image': '',
            'media': '',
            'views': 0,
            'user': {
                'owner': '',
                'members': [
                    ''
                ],
            },
            'trending': 0,
            'rating'' : {
                'quality_score': 0,
                'opinion_score': 0,
                'relevance_score': 0,
                'opinion_votes': 0,
                'quality_votes': 0,
                'relevance_votes': 0
            }
        }
    elif settings_req == "db_collection_user":
        return {
            'alias': '',
            'firstname': '',
            'lastname': '',
            'email': '',
            'desc': '',
            'tokens' '',
            'nodes': [
                ''
            ],
            'image': '',
            'views': 0,
            'weekly': 0,
            'trending': 0,
            'flags': {
                'level': 0,
                'comment': ''
            },
            'created_on': 0,
            'updated_on': 0
        }
    elif settings_req == "db_collection_tags":
        return {
            'name': '',
            'desc': '',
            'nodes': [ 
                ''
            ],
            'created_on': 0,
            'updated_on': 0
        }
    #settings_req didnt meet any of the listed variables
    else:
        return False