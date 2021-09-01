from pyfirmata2 import Arduino,util
import tkinter
from time import sleep

board = Arduino('/dev/cu.usbmodem14201')

PINS = [0]

def onStartButtonPress():
    timePeriod = timePeriodEntry.get()
    timePeriod = float(timePeriod)
    ledBrightness = brightnessScale.get()
    ledBrightness = float(ledBrightness)
    startButton.config(state=tkinter.DISABLED)
    board.get_pin('d:11:p').write(ledBrightness/100.0)
    sleep(timePeriod)
    ######board.get_pin('d:11:p').write(0)
    startButton.config(state=tkinter.ACTIVE)
    
top = tkinter.Tk()
top.title("Tiempo:")
timePeriodEntry = tkinter.Entry(top, bd = 5, width = 25)
timePeriodEntry.pack()
timePeriodEntry.focus_set()

brightnessScale = tkinter.Scale(top, from_=0, to =100, orient=tkinter.HORIZONTAL)
brightnessScale.pack()

startButton = tkinter.Button(top, text="Start", command= onStartButtonPress)
startButton.pack()
top.mainloop()

print ("Conectando al Arduino...")
it = util.Iterator(board)
it.start()

for pin in PINS:
    board.analog[pin].enable_reporting()
    
while 1:
    for pin in PINS:
        print (f"Pin a{pin} : {board.analog[pin].read()}")
    board.pass_time(1)
