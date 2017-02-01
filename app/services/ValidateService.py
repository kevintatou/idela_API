from bson import ObjectId

#Validates a dictionary for mongodb query use
#Recieves dictionary in a normal format
#Returns a dictionary with dictionaries inside
def ValidateGetTerms(dict1):
    #Defining variables
    attribute = {}
    result = {}
    
    #Allowed terms and type to be used when calling database
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

    #Query to find multiple objects by ObjectIds
    #result = collection.find({"_id":{ "$in": [id, id]}})

    #1. Checks if items in URL are legal
    for term in allowed_terms:
        for dict1_item in dict1:
            if dict1_item == term:
                #Changes values in dict1 to int if allowed_terms says it is
                if allowed_terms.get(term) == int:
                    attribute[dict1_item] = int(dict1.get(dict1_item))
                    result['attribute'] = attribute
                else:
                    #Changes id key and value to proper attributes for mongodb use
                    if dict1_item == 'id':
                        attribute['_id'] = ObjectId(dict1.get(dict1_item))
                        result['attribute'] = attribute
                    #Changes col key and puts value in it 
                    elif dict1_item == 'col':
                        result['collection'] = [dict1.get(dict1_item)]
                    #Puts value in select key
                    elif dict1_item == 'select':
                        result['select'] = [dict1.get(dict1_item)]
                    else:
                        attribute[dict1_item] = dict1.get(dict1_item)
                        result['attribute'] = attribute

    return result