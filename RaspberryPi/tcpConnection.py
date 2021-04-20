import socket
import json

from database import ClearDatabase
from config import SetTimeConfig

TCP_PORT = 5005
BUFFER_SIZE = 1024
TCP_IP = "192.168.88.88"
 
###Send#######################################################################

def SendData(data):
    """Send Data over TCP => Use JSON Format"""

    try:
        conn.send(str.encode(str(data)))
        conn.recv(BUFFER_SIZE)
        conn.send(str.encode(str("stop")))
        return True

    except:
        print("database.json is needed!\nError: SendData")
        return False  


def SendAllData():
    """Send Data over TCP => Use JSON Format"""

    try:
        # Json Config File einbinden
        file = open("database.json", "r")  

        data = json.dumps(json.load(file))     
        data = str(data)
        dataB = str.encode(data)
        conn.send(dataB)
        file.close()
        return True

    except:
        print("database.json is needed!\nError: SendData")
        return False  


def SendDataTemperature(interval):
    """Send Data over TCP => Use JSON Format"""

    try:
        # Json Config File einbinden
        file = open("database.json", "r")  

        data = json.load(file)    

        data = data["temperature"]

        i = 0

        for x in data:
            if i == interval:
                conn.send(str.encode(str(x)))
                conn.recv(BUFFER_SIZE)
                i = 1
            else:
                i = i + 1
        conn.send(str.encode(str("stop")))
        file.close()
        return True

    except:
        print("database.json is needed!\nError: SendDataTemperature")
        return False 


def SendDataHumidity(interval):
    """Send Data over TCP => Use JSON Format"""

    try:
        # Json Config File einbinden
        file = open("database.json", "r")       

        data = json.load(file)    

        data = data["humidity"]

        i = 0

        for x in data:
            if i == interval:
                conn.send(str.encode(str(x)))
                conn.recv(BUFFER_SIZE)
                i = 1
            else:
                i = i + 1
        conn.send(str.encode(str("stop")))
        file.close()
        return True

    except:
        print("database.json is needed!\nError: SendDataHumidity")
        return False 


def SendDataPressure(interval):
    """Send Data over TCP => Use JSON Format"""

    try:
        # Json Config File einbinden
        file = open("database.json", "r")  

        data = json.load(file)

        data = data["pressure"]

        i = 0

        for x in data:
            if i == interval:
                conn.send(str.encode(str(x)))
                conn.recv(BUFFER_SIZE)
                i = 1
            else:
                i = i + 1
        conn.send(str.encode(str("stop")))
        file.close()
        return True

    except:
        print("database.json is needed!\nError: SendDataPressure")
        return False 


def SendDataName():
    """Send Data over TCP => Use JSON Format"""

    try:
        # Json Config File einbinden
        file = open("database.json", "r")  

        data = json.load(file)     

        data = data["name"]
        conn.send(str.encode(str(data)))
        conn.recv(BUFFER_SIZE)
        conn.send(str.encode(str("stop")))
        file.close()
        return True

    except:
        print("database.json is needed!\nError: SendDataName")
        return False 


def SendDataStructs():
    """Send Data over TCP => Use JSON Format"""

    try:
        # Json Config File einbinden
        file = open("database.json", "r")  

        data = json.load(file)     

        data = data["structs"]
        conn.send(str.encode(str(data)))
        conn.recv(BUFFER_SIZE)
        conn.send(str.encode(str("stop")))
        file.close()
        return True

    except:
        print("database.json is needed!\nError: SendDataStructs")
        return False 

def SendDataConfig():
    """Send Data over TCP => Use JSON Format"""

    try:
        # Json Config File einbinden
        file = open("database.json", "r")  

        data = json.load(file)     

        data = data["config.json"]
        conn.send(str.encode(str(data)))
        conn.recv(BUFFER_SIZE)
        conn.send(str.encode(str("stop")))
        file.close()
        return True

    except:
        print("database.json is needed!\nError: SendDataConfig")
        return False 
################################################################################


def ReseveData():
    """Reseve Data over TCP => In JSON Format"""    

    dataResv = conn.recv(BUFFER_SIZE)
        #if not dataResv: break
    print("received data:", dataResv)

        #if dataResv != 0: break
        
    return dataResv


def OpenTCPConnection():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((TCP_IP, TCP_PORT))
        s.listen()
        print("Wait for connection")

        global conn
        conn, addr = s.accept()
        print('Connection address:', addr)

        return True

    except:
        #print("No connection to tcp client")
        #CloseTCPConnection()
        return False

def CloseTCPConnection():
    try:
        conn.close()
        return True

    except:
        print("Close TCP connection faild")
        return False

def TCP():

    OpenTCPConnection()           

    data = ReseveData()
        
    if data == str.encode("data"):
        SendAllData()

    ###SendDataTemperature####################################

    elif data == str.encode("temperature 1"):
        SendDataTemperature(1)

    elif data == str.encode("temperature 2"):
        SendDataTemperature(2)

    elif data == str.encode("temperature 5"):
        SendDataTemperature(5)

    elif data == str.encode("temperature 10"):
        SendDataTemperature(10)

    elif data == str.encode("temperature 50"):
        SendDataTemperature(50)

    elif data == str.encode("temperature 100"):
        SendDataTemperature(100)

    ###SendDataHumidity####################################

    elif data == str.encode("humidity 1"):
        SendDataHumidity(1)
            
    elif data == str.encode("humidity 2"):
        SendDataHumidity(2)

    elif data == str.encode("humidity 5"):
        SendDataHumidity(5)

    elif data == str.encode("humidity 10"):
        SendDataHumidity(10)

    elif data == str.encode("humidity 50"):
        SendDataHumidity(50)

    elif data == str.encode("humidity 100"):
        SendDataHumidity(100)

    ###SendDataPressure####################################

    elif data == str.encode("pressure 1"):
        SendDataPressure(1)

    elif data == str.encode("pressure 2"):
        SendDataPressure(2)

    elif data == str.encode("pressure 5"):
        SendDataPressure(5)

    elif data == str.encode("pressure 10"):
        SendDataPressure(10)

    elif data == str.encode("pressure 50"):
        SendDataPressure(50)

    elif data == str.encode("pressure 100"):
        SendDataPressure(100)

    #######################################

    elif data == str.encode("clear"):
        if ClearDatabase():
            SendData("true")
        else:
            SendData("false")

    elif data == str.encode("name"):
        SendDataName()

    elif data == str.encode("structs"):
        SendDataStructs()

    elif data == str.encode("config"):
        SendDataConfig()

    #1 Minute
    elif data == str.encode("time 1"):
        print("time set: 1 Minute")
        SendData(SetTimeConfig(60))
            

    #5 Minuten
    elif data == str.encode("time 5"):
        print("Time Set: 5 Minuten")
        SendData(SetTimeConfig(300))
            

    #10 Minuten
    elif data == str.encode("time 10"):
        print("Time Set: 10 Minuten")
        SendData(SetTimeConfig(600))
            

    #30 Minuten
    elif data == str.encode("time 30"):
        print("Time Set: 30 Minuten")
        SendData(SetTimeConfig(1800))
            

    #1 Stunde
    elif data == str.encode("time 60"):
        print("Time Set: 1 Stunde")
        SendData(SetTimeConfig(3600))
            

    #6 Stunden
    elif data == str.encode("time 360"):
        print("Time Set: 6 Stunde")
        SendData(SetTimeConfig(21600))
            

    #12 Stunden
    elif data == str.encode("time 720"):
        print("Time Set: 12 Stunde")
        SendData(SetTimeConfig(43200))
            

    #24 Stunden
    elif data == str.encode("time 1440"):
        print("Time Set: 24 Stunde")
        SendData(SetTimeConfig(86400))
            

    else:
        CloseTCPConnection()        

    