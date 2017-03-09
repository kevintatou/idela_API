from app.services.conn import *
import datetime

# Posts data into given entity's collection

'''
def InsertData(*args):
    args[1]['date'] = datetime.datetime.utcnow()
    args[0].insert_one(args[1])
'''

def PostRequest(request):
    print(request)
    node.insert_one(request)


