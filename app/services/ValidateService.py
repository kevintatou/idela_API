from bson import ObjectId

#Validates a dictionary for mongodb query use
#Recieves dictionary in a normal format
#Returns a dictionary with dictionaries inside
def ValidateGetTerms(dict1):
    #Defining variabless
    attribute = {}
    result = {}
    
    #Allowed terms with type to be used when calling database
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

    #1. Checks if items in URL are legal
    for term in allowed_terms:
        for dict1_item in dict1:
            if dict1_item == term:
                if allowed_terms.get(term) == int:
                    attribute[dict1_item] = int(dict1.get(dict1_item))
                    result['attribute'] = attribute
                else:
                    #Converts id key and value to proper attributes for mongodb use
                    if dict1_item == 'id':
                        attribute['_id'] = ObjectId(dict1.get(dict1_item))
                        result['attribute'] = attribute
                    #Puts
                    elif dict1_item == 'col':
                        result['collection'] = [dict1.get(dict1_item)]
                    elif dict1_item == 'select':
                        result['select'] = [dict1.get(dict1_item)]
                    else:
                        attribute[dict1_item] = dict1.get(dict1_item)
                        result['attribute'] = attribute

    return result