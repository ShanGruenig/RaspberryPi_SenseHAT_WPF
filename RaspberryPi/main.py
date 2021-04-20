from datetime import datetime
import json
import os
import time
import threading

from database import GetData
from database import LoadDatabase
from tcpConnection import TCP
from SenseHAT import SenseHat


###Threading############################################################################

class ThreadingGetData():

    def __init__(self):
        """Init Threads"""
        try:
            # Thread erstellen der im Hintergrund läuft und danach starten
            thread = threading.Thread(target=self.run, args=(), daemon=True)
            thread.start()
            print("Thread GetData Started")

        except:
            print("Can't create Tread")

    def run(self):
        """Run Threads"""
        while True:
            try:
                # IPs aktuallisieren und Intervall abwarten (Thread im Hintergrund)
                GetData()
                time.sleep(int(configFile.get("time")) - 60)#int(configFile.get("Time")) - 60
 
            except Exception as e:
                print(f"Error Threading GetData \nError: {e}")


class ThreadingTCP():

    def __init__(self):
        """Init Threads"""
        try:
            # Thread erstellen der im Hintergrund läuft und danach starten
            thread = threading.Thread(target=self.run, args=(), daemon=True)
            thread.start()
            print("Thread TCP Started")

        except:
            print("Can't create Tread")

    def run(self):
        """Run Threads"""
        while True:
            try:
                # IPs aktuallisieren und Intervall abwarten (Thread im Hintergrund)
                time.sleep(1)
                TCP()
 
            except:
                pass


class ThreadingSenseHAT(): 

    def __init__(self):
        """Init Threads"""
        try:
            # Thread erstellen der im Hintergrund läuft und danach starten
            thread = threading.Thread(target=self.run, args=(), daemon=True)
            thread.start()
            print("Thread SenseHAT Started")

        except:
            print("Can't create Tread")

    def run(self):
        """Run Threads"""

        while True:
            try:
                # IPs aktuallisieren und Intervall abwarten (Thread im Hintergrund)
                time.sleep(1)
                SenseHat()
 
            except Exception as e:
                print(f"Error Threading SenseHAT \nError: {e}")


###Main########################################################################
if __name__ == "__main__":     

    LoadDatabase()    

    # Im Hintergrund Threads laufen lassen
    threadGetData = ThreadingGetData()
    threadTCP = ThreadingTCP()
    threadSenseHAT = ThreadingSenseHAT()

    #Main Thread make this:
    while True:

        try:
            # Json Config File einbinden
            file = open("config.json", "r") 
            global configFile
            configFile = json.load(file)
            file.close()
            #print("ConfigFile loaded\n")

        except:
            print("Config.json is needed!" + "\n\n")

        try:
            # Interval zum abwarten
            time.sleep(int(configFile.get("interval"))) 

        except:
            print("Error Interval")

