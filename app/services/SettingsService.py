#Overall useful variables
def SettingsHandler(settings_req):
    #Allowed terms to be used for mongodb use
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
    
    #Mongodb collections
    db_collections = [
        'user',
        'node',
        'tag',
        'softdelete',
        'feedback'
    ]

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