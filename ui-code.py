# Importing necessary modules
from tkinter import *
from time import sleep
import Adafruit_DHT
import RPi.GPIO as GPIO
import board

#Set UI temperature and moisture
global custom_temperature = 20
global custom_moisture = 0

# set up sensor input
GPIO.setmode(GPIO.BCM)
TEMP_INPUT = 21
MOISTURE_INPUT = 18
DHT_SENSOR = Adafruit_DHT.DHT22
GPIO.setup(MOISTURE_INPUT, GPIO.IN)
GPIO.setup(TEMP_INPUT, GPIO.IN)
while True:
    actual_moisture = GPIO.input(MOISTURE_INPUT)
    print(actual_moisture)
    humidity, actual_temperature = Adafruit_DHT.read_retry(DHT_SENSOR, TEMP_INPUT)
    print(actual_temperature)
    if actual_temperature < custom_temperature - 1:
        print("Plant is too cold")
    elif actual_temperature > custom_temperature + 1:
        print("Plant is too hot")
    if actual_moisture == 0:
        print("Plant is dry. Turning on hose")
    elif actual_moisture == 1:
        print("Plant is damp enough")
    sleep(1)

# =======================================================
# Edit these variables to modify the UI elements
# These variables are for easier modification to the UI
# =======================================================

# The window title
windowTitle = 'SmartPot Control'

# Header text font and font size
hFont = 'Arial'
hFontSize = 12

# Sensor reading values text font and font size
vFont = 'Arial'
vFontSize = 27

# Temperature label header text
hTempText = 'Temperature'

# Moisture label header text
hMoistText = 'Moisture'

# Adjustment title label text & font properties
adjustmentTitle = 'Adjust Temperature/Moisture'
atFont = 'Arial'
atFontSize = 12

# Button texts
buttonRaiseTemp = 'RAISE'
buttonLowerTemp = 'LOWER'
buttonRaiseMoisture = 'RAISE'
buttonLowerMoisture = 'LOWER'

# Button text font properties
buttonFont = 'Arial'
buttonFontSize = 10


# Function that will be called when pressing the buttons
# Button for increasing temperature
def increaseTemperature():
    custom_temperature += 1
    result = str(custom_temperature) + "°C"
    lblTempVal.config(text = result)


# Button for lowering temperature
def lowerTemperature():
    custom_temperature -= 1
    result = str(custom_temperature) + "°C"
    lblTempVal.config(text = result)


# Button for increasing moisture level
def increaseMoisture():
    custom_moisture += 1
    result = str(custom_moisture) + "%"
    lblMoistVal.config(text = result)


# Button for lowering moisture level
def lowerMoisture():
    custom_moisture -= 1
    result = str(custom_moisture) + "%"
    lblMoistVal.config(text = result)


# =======================================================
# End
# Please handle everything below this line with care
# =======================================================

window = Tk()
window.title(windowTitle)       # The title of the window
window.geometry('384x288')      # 4:3 resolution
window.resizable(False, False)  # Make the window impossible to be resized

# Label definitions
# Label for temperature header text
lblTempHeader = Label(
    text=hTempText,
    font=(hFont, hFontSize),
    fg='white',
    bg='grey',
    width=12,
    height=2
)

# Label for moisture header text
lblMoistHeader = Label(
    text=hMoistText,
    font=(hFont, hFontSize),
    fg='white',
    bg='grey',
    width=12,
    height=2
)

# Label for temperature value
lblTempVal = Label(
    text=custom_temperature + "°C",
    font=(vFont, vFontSize),
    fg='black',
    bg='white',
    width=5,
    height=1
)

# Label for moisture level value
lblMoistVal = Label(
    text=custom_moisture + "%",
    font=(vFont, vFontSize),
    fg='black',
    bg='white',
    width=5,
    height=1
)

# Label for adjustment title header
lblAdjustTitle = Label(
    text=adjustmentTitle,
    font=(atFont, atFontSize),
    fg='white',
    bg='grey',
    width=25,
    height=1
)

# Button definitions
# Increase temperature button
btnUpTemp = Button(
    text=buttonRaiseTemp,
    font=(buttonFont, buttonFontSize),
    width=8,
    height=2,
    command=increaseTemperature
)

# Lower temperature button
btnLowerTemp = Button(
    text=buttonLowerTemp,
    font=(buttonFont, buttonFontSize),
    width=8,
    height=2,
    command=lowerTemperature
)

# Increase moisture level button
btnUpMoist = Button(
    text=buttonRaiseMoisture,
    font=(buttonFont, buttonFontSize),
    width=8,
    height=2,
    command=increaseMoisture
)

# Lower moisture level button
btnLowerMoist = Button(
    text=buttonLowerMoisture,
    font=(buttonFont, buttonFontSize),
    width=8,
    height=2,
    command=lowerMoisture
)

# Header labels placements
lblTempHeader.place(x=75, y=5)
lblMoistHeader.place(x=195, y=5)

# Sensor reading value labels placements
lblTempVal.place(x=76, y=50)
lblMoistVal.place(x=196, y=50)

# Adjustment title text label placement
lblAdjustTitle.place(x=76, y=100)

# Button placements
btnUpTemp.place(x=88, y=150)
btnLowerTemp.place(x=88, y=195)
btnUpMoist.place(x=215, y=150)
btnLowerMoist.place(x=215, y=195)

window.mainloop()
