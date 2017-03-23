from app.services.conn import *

#Gets data from DB
#IN: name of collection (required), what to search by, which field to select
#OUT: Query result from DB
def GetRequest(col, find, select=None):
    
    if select is not None:
        result = eval(col).find(find).distinct(select)
    elif col is not None:
        result = eval(col).find(find)
    
    return result