from sense_hat import SenseHat
from temperature import GetTemperature
from humidity import GetHumidity
from pressure import GetPressure

sense = SenseHat()

def read_temp():
    temperature = GetTemperature()
   # print("Temperatur: " + temperature + " °C")
    sense.show_message(temperature)
    sense.clear()

def read_humi():
    humidity = GetHumidity()
   # print("Luftfeuchtigkeit: " + humidity + " %")
    sense.show_message(humidity)
    sense.clear()

def read_pres():
    pressure = GetPressure()  
   # print("Luftdruck: " + pressure + " mBar")
    sense.show_message(pressure)
    sense.clear()

def SenseHat():    
    sense.stick.direction_up = read_temp
    sense.stick.direction_right = read_humi
    sense.stick.direction_down = read_pres
    sense.stick.direction_middle = sense.clear