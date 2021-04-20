from sense_hat import SenseHat

sense = SenseHat()

string = "{form:.2f}"

def GetHumidity():
    try:
        humidity = string.format(form = sense.get_humidity())        
        return humidity

    except:
        return 0
