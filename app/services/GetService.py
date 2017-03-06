from app.services.conn import *

    #Query to find multiple objects by ObjectIds
    #value_list = [id, id]
    #result = args[3].find({"_id":{ "$in": value_list}})

def GetRequest(req_values):
    #Define variables
    select = None
    collection = None
    attribute = None
    
    #Check for existing keys and adds those values into a variable
    for item in req_values:
        if item == 'select':
            select = req_values['select'][0]
        elif item == 'collection':
            collection = eval(req_values['collection'][0])
        elif item == 'attribute':
            attribute = req_values['attribute']
    
    if select != None:
        result = collection.find(attribute).distinct(select)
    elif collection != None:
        result = collection.find(attribute)

    return result
