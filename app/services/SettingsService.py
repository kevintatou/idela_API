#Overall useful variables
def SettingsHandler(settings_req):
    #Allowed terms to be used for MongoDB use
    if settings_req == "allowed_keys":
        return allowed_keys = {
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
        return db_collections = [
            'user',
            'node',
            'tag',
            'softdelete',
            'feedback'
        ]
    #Minimum requirements for Node creation
    elif settings_req == "min_node_req":
        return min_node_req = [
            'tags',
            'name',
            'public',
            'owner'
        ]
    #Minimum requirements for User creation
    elif settings_req == "min_user_req":
        return min_user_req = [
            'firstname',
            'lastname',
            'email',
            'tokens'
        ]
    #Minimum requirements for Tag creation
    elif settings_req == "min_tag_req":
        return min_tag_req = [
            'name'
        ]
    #MongoDB structure for Node collection
    elif settings_req == "db_collection_node":
        return db_collection_node = {
            "date": int,
            "weekly": int,
            "tags": [
                str
            ],
            "desc": str,
            "flags": {
                "comment": str,
                "rating": str
            },
            "name": str,
            "public": int,
            "token": str,
            "image": str,
            "media": str,
            "views": int,
            "users": {
                "owner": str,
                "members": [
                    str
                ]
            },
            "trending": int,
            "rating": {
                "quality_score": int,
                "opinion_score": int,
                "relevance_score": int,
                "opinion_votes": int,
                "quality_votes": int,
                "relevance_votes": int
            }
        }
    #settings_req didnt meet any of the listed variables
    else:
        return False