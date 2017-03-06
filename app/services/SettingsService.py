#Overall useful variables
def SettingsHandler(settings_req):
    #Allowed terms to be used for MongoDB use
    allowed_terms = {
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
    db_collections = [
        'user',
        'node',
        'tag',
        'softdelete',
        'feedback'
    ]

    #MongoDB structure for Node collection
    db_collection_node = {
        "date": int,
        "weekly": int,
        "tags": [str],
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
            "members": [str]
        },
        "trending": int,
        "rating": {
            "quality_score": int ,
            "opinion_score": int ,
            "relevance_score": int ,
            "opinion_votes": int ,
            "quality_votes": int ,
            "relevance_votes": int
        }
    }

    #db_collection_node = {}
    #db_collection_user = {}
    #db_collection_tag = {}
    #db_collection_softdelete = {}
    #db_collection_feedback = {}

    #Checks what was requested and returns request variable
    if settings_req == 'allowed_terms':
        return allowed_terms
    elif settings_req == 'db_collections':
        return db_collections
    elif settings_req == 'db_collection_node':
        return db_collection_node