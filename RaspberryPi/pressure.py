from sense_hat import SenseHat

sense = SenseHat()

string = "{form:.2f}"

def GetPressure():
    try:
        pressure = string.format(form = sense.get_pressure())
        return pressure

    except:
        return 0