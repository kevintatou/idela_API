from app.services.conn import *
import datetime

############# TO DO #############
#Remove loop
#Make push and set more dynamic

#Updates the current data with more data by adding to the existing data
#IN: Where, cursor with _id, Dict with push data
def UpdateRequest(col, document_id, push_dict):
    eval(col).update({
        '_id': document_id
    },{
        '$push': push_dict,
        '$set': {'updated': datetime.datetime.now()}
    }, upsert=False, multi=False )