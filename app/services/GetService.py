from app.services.conn import *

    #Query to find multiple objects by ObjectIds
    #value_list = [id, id]
    #result = args[3].find({"_id":{ "$in": value_list}})

#Gets data from DB
#IN: Dict with 3 keys(collection, attribute, select) containing information
#OUT: Query result from DB
def GetRequest(req_values):
    
    #Define variables
    select = None
    collection = None
    attribute = None
    
    #Check for existing keys and adds those values into a variable
    for key in req_values:
        if key == 'select':
            select = req_values['select'][0]
        elif key == 'collection':
            #Using eval to convert str to 'python code'
            collection = eval(req_values['collection'][0])
        elif key == 'attribute':
            attribute = req_values['attribute']
    
    if select != None:
        result = collection.find(attribute).distinct(select)
    elif collection != None:
        result = collection.find(attribute)

    return result
