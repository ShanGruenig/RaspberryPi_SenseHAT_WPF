from sense_hat import SenseHat

sense = SenseHat()

string = "{form:.2f}"

def GetTemperature():
    try:
        temperature = string.format(form = sense.get_temperature() - 8)
        return temperature

    except:
        return 0
