from app.services.conn import *

def UpdateRequest(request, col):
    decoded_doc = bson.BSON.decode(request)
    '''eval(col).update({
        '_id': request['_id']
        },{
        '$set': {
            'nodes': 'hej'
        }
    }, upsert=False, multi=False)'''