
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

def FormatMultipleGetValues(request):
    for key in request:
        request[key] = request[key].split(",")

        if len(request[key]) > 1:
            request[key] = {"$in" : request[key]}
        else:
            request[key] = str(request[key][0])
    
    return request