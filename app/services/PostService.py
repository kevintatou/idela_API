from app.services.conn import *
import datetime

# Posts data into given entity's collection
def PostRequest(request, col):
    #Timestamp
    request['created_on'] = datetime.datetime.utcnow()

    print(request)
    #col.insert_one(request)


