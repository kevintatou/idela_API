from app.services import SettingsService, GetService, PostService, UpdateService
from bson import ObjectId
from copy import copy
import datetime

############# TO DO #############
#Figure out something better

def ValidateLegalKeys(request, allowed_keys, result={}):
    tmp_list = []
    for key in allowed_keys:
        if key in request:
            if key == 'id':
                if type(request.get(key)) is dict:
                    for item in request.get(key)['$in']:
                        item = ObjectId(item)
                        tmp_list.append(item)
                        result['_id'] = {}
                        result['_id']['$in'] = tmp_list
                else:
                    result['_id'] = ObjectId(request.get(key))
            elif allowed_keys.get(key) == int:
                if type(request.get(key)) is dict:
                    for item in request.get(key)['$in']:
                        item = int(item)
                        tmp_list.append(item)
                        result[key] = {}
                        result[key]['$in'] = tmp_list
                else:
                    result[key] = int(request.get(key))
            elif allowed_keys.get(key) == str:
                if type(request.get(key)) is dict:
                    for item in request.get(key)['$in']:
                        item = str(item)
                        tmp_list.append(item)
                        result[key] = {}
                        result[key]['$in'] = tmp_list
                else:
                    result[key] = int(request.get(key))
    
    return result
    

#Checks if the request meets the minimum requirements
#IN: Simple dictionary, collection
#OUT: Bool
def ValidateMinRequire(request, min_requirement):
    
    #Checks if min_requirement keys exist in request, If not return False
    for key in min_requirement:
        if key not in request: 
            return False
    
    return True
