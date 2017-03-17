from app.services.conn import *

#IN: Where, WhatToUpdate
def UpdateRequest(request, col):
    print("-------------------------------------")
    
    for item in request:
        print(item)
        '''
        eval(col).update({
            '_id': item['_id']
            },{
            '$set': {
                'nodes': 'wwww'
            }
        }, upsert=False, multi=False
        '''