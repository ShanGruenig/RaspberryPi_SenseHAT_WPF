from datetime import datetime
import json
import time

from temperature import GetTemperature
from humidity import GetHumidity
from pressure import GetPressure

###Globale Variabeln####################################################################

jsonDataConst = {"name" : "database.json", "structs" : {"time" : "timestruct : %d-%m-%Y %H:%M:%S", "temperature" : "double", "humidity" : "double", "pressure" : "double"}, "config.json" : {"time" : "60", "interval" : "60"}, "temperature" : [], "humidity" : [], "pressure" : []}
jsonData = {}

###Class############################################################################

def DataToDatabase():
    """Load Data to Database => database.json"""
    try:
        file = open("database.json", "w")
        database = json.dump(jsonData, file, indent=4) 
        file.close()      

    except:
        print("Error")

def DataToList(temp, humid, pres):
    """Apped Sensor Data to a List => For Load in Database use DataToDatabase()"""
    try:
        jsonData["temperature"].append({"time" : datetime.now().strftime("%d-%m-%Y %H:%M:%S"), "temperature" : temp})
        jsonData["humidity"].append({"time" : datetime.now().strftime("%d-%m-%Y %H:%M:%S"), "humidity" :  humid})
        jsonData["pressure"].append({"time" : datetime.now().strftime("%d-%m-%Y %H:%M:%S"), "pressure" : pres})

    except:
        print("No Data apped to List")
        return False

def DataConfigToList(time):
    """Apped Time Data to a List => For Load in Database use DataToDatabase()"""
    try:
        jsonData["config.json"] = {"time" : str(time), "interval" : "60"}

    except:
        print("No Data apped to List")
        return False

def LoadDatabase():
    """Load Database => database.json"""
    try:
        # Json Config File einbinden
        file = open("database.json", "r") 
        global jsonData
        jsonData = json.load(file)  
        print("Database loaded")
        file.close()
        return True

    except:
        print("database.json is needed!" + "\n\n")
        return False

def ClearDatabase():
    try:
        global jsonData

        jsonData.clear()
        jsonData = jsonDataConst

        return True

    except:
        print("Error: ClearDatabase")
        return False

###Get Data####################################################################

def GetData():

    GetConfigFile()    

    none = GetHumidity()
    time.sleep(1)

    dataT1 = GetTemperature()
    dataH1 = GetHumidity()
    dataP1 = GetPressure()
    time.sleep(timer)

    GetConfigFile()

    dataT2 = GetTemperature()
    dataH2 = GetHumidity()
    dataP2 = GetPressure()
    time.sleep(timer)

    GetConfigFile()
    
    dataT3 = GetTemperature()
    dataH3 = GetHumidity()
    dataP3 = GetPressure()
    time.sleep(timer)

    GetConfigFile()

    dataT4 = GetTemperature()
    dataH4 = GetHumidity()
    dataP4 = GetPressure()
    time.sleep(timer)

    GetConfigFile()

    dataT5 = GetTemperature()
    dataH5 = GetHumidity()
    dataP5 = GetPressure()
    time.sleep(timer)

    GetConfigFile()
    
    dataT6 = GetTemperature()
    dataH6 = GetHumidity()
    dataP6 = GetPressure()
    time.sleep(timer)

    GetConfigFile()
           
    dataT7 = GetTemperature()
    dataH7 = GetHumidity()
    dataP7 = GetPressure()
    time.sleep(timer)

    GetConfigFile()

    dataT8 = GetTemperature()
    dataH8 = GetHumidity()
    dataP8 = GetPressure()
    time.sleep(timer)

    GetConfigFile()

    dataT9 = GetTemperature()
    dataH9 = GetHumidity()
    dataP9 = GetPressure()
    time.sleep(timer)

    dataT10 = GetTemperature()
    dataH10 = GetHumidity()
    dataP10 = GetPressure()

    #Durchschnittswert rechnen
    stringFormat = "{form:.2f}"

    temperature = stringFormat.format(form = (float(dataT1) + float(dataT2) + float(dataT3) + float(dataT4) + float(dataT5) + float(dataT6) + float(dataT7) + float(dataT8) + float(dataT9) + float(dataT10)) / 10)
    humidity = stringFormat.format(form = (float(dataH1) + float(dataH2) + float(dataH3) + float(dataH4) + float(dataH5) + float(dataH6) + float(dataH7) + float(dataH8) + float(dataH9) + float(dataH10)) / 10)
    pressure = stringFormat.format(form = (float(dataP1) + float(dataP2) + float(dataP3) + float(dataP4) + float(dataP5) + float(dataP6) + float(dataP7) + float(dataP8) + float(dataP9) + float(dataP10)) / 10)

    DataToList(temperature, humidity, pressure)

    DataToDatabase()


def GetConfigFile():
    try:
        # Json Config File einbinden
        file = open("config.json", "r") 
        global configFile
        global timer
        configFile = json.load(file)
        timer = float(configFile.get("time")) / 9
        file.close()

    except:
        print("Config.json is needed! GetConfigFile" + "\n\n")
