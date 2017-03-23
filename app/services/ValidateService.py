from app.services import SettingsService, GetService, PostService, UpdateService

#Checks if the request meets the minimum requirements
#IN: Simple dictionary, collection
#OUT: Bool
def ValidateMinRequire(request, min_requirement):
    
    #Checks if min_requirement keys exist in request, If not return False
    for key in min_requirement:
        if key not in request: 
            return False
    
    return True
