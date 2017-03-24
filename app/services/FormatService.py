from bson import ObjectId

#Turns a simple dict to a sturctured one
#IN: Simple dictionary to structure and a structured dict as a guide
#OUT: A structured dict
def FormatDict(request, structure):
    for key in structure:
        #If the structure key is a dict call this function with the embedded structure keys
        if type(structure[key]) is dict:
            FormatDict(request,structure[key])
        else:
            #Loops through the request and adds values to the proper places
            if key in request:
                if type(structure[key]) == str:
                    structure[key] = str(request[key])
                elif type(structure[key]) == int:
                    structure[key] = int(request[key])
                elif type(structure[key]) is list:
                    structure[key] = request[key].split(" ")

    return structure

#Splits values for MongoDB use
#IN: Dict with key and value(s) 
#OUT: Dict with splited values
def MongoDBifyMutliGetValues(request):
    for key in request:
        #If value is str split into a list
        if type(request[key]) is str:
            request[key] = request[key].split(",")

        #If the split made more than a total of 1 items add $in
        if len(request[key]) > 1:
            request[key] = {"$in" : request[key]}
        #Else make it a string 
        else:
            request[key] = str(request[key][0])
    
    return request

#
#IN:
#OUT:
def FormatLegalKeys(request, allowed_keys):
    result={}
    tmp_list=[]
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
                    result[key] = str(request.get(key))
    
    return result