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
    elif settings_req == "min_tag_req":
        return  [
            'name'
        ]
    #MongoDB structure for Node collection
    elif settings_req == "db_collection_node":
        return {
            "date": int,
            "weekly": int,
            "tags": [
                str
            ],
            "desc": str,
            "flags": {
                "comment": str,
                "rating": str,
            },
            "name": str,
            "public": int,
            "token": str,
            "image": str,
            "media": str,
            "views": int,
            "user": {
                "owner": str,
                "members": [
                    str
                ],
            },
            "trending": int,
            "rating" : {
                "quality_score": int,
                "opinion_score": int,
                "relevance_score": int,
                "opinion_votes": int,
                "quality_votes": int,
                "relevance_votes": int
            }
        }
    elif settings_req == "db_collection_user":
        return {

        }
    elif settings_req == "db_collection_tag":
        return {

        }
    #settings_req didnt meet any of the listed variables
    else:
        return False