import json

from database import DataConfigToList
from database import DataToDatabase

#####################################################################
jsonDataConst = {"time" : "60", "interval" : "60"}
jsonData = {"time" : "60", "interval" : "60"}
###Class############################################################################

def DataToConfig():
    """Load Data to config.json => config.json"""
    try:
        file = open("config.json", "w")
        config = json.dump(jsonData, file, indent=4)
        file.close()    

    except:
        print("Error")


def SetTimeConfig(time):
    try:
        global jsonData
        jsonData = {"time" : str(time), "interval" : "60"}
        DataConfigToList(time)
        DataToDatabase()
        DataToConfig()
        return True

    except:
        print("Error Set Time Config")
        return False

