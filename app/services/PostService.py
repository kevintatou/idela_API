from app.services.conn import *
import datetime

# Posts data into given entity's collection


def InsertData(*args):
    args[1]['date'] = datetime.datetime.utcnow()
    args[0].insert_one(args[1])
    
def PostRequest(req_values):
    print("PostRequest")


'''
def InsertData(req_values):
    #Defining variables
    collection = None
    attribute = None

    for item in req_values:
        if item == 'collection':
            collection = eval(req_values['collection'][0])
        elif item == 'attribute':
            attribute = req_values['attribute']
    
    #attribute['date'] = datetime.datetime.utcnow()

    print(attribute)
    
    test = {
        name: 'name'
    }

    node.insert_one(test)
'''

