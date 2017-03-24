from app.services.conn import *
import datetime

#IN: Formated dict for post request use
#OUT: The post request with ObjectID
#Posts data into given entity's collection
def PostRequest(request, col):
    #Timestamp
    request['created'] = datetime.datetime.utcnow()

    eval(col).insert(request)

    return request

#IN: Formated dicts in a list for post request use
#OUT: The post requests with ObjectIDs
#Post multiple documents at once(Single documents does work too)
def PostRequestMany(request, col):
    print(request)
    #Timestamp every dict in the request list
    for item in request:
        item['created'] = datetime.datetime.utcnow()
    
    eval(col).insert_many(request).inserted_ids

    return request
