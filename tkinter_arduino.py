from pyfirmata2 import Arduino,util
import time
import tkinter

board = Arduino('/dev/cu.usbmodem14201')
ledPin = board.get_pin('d:11:p')

it = util.Iterator(board)
it.start()
potentiometer = board.analog[0]
potentiometer.enable_reporting()

def onStartButtonPress():
    while True:
        if flag.get():
            analogReadLabel.config(text=str(potentiometer.read()))
            analogReadLabel.update_idletasks()
            top.update()
            print("Lectura del potenciómetro")
            print(F"a0: {potentiometer.read()}")
            ledPin.write(potentiometer.read())
            time.sleep(0.1)
            startButton.config(state=tkinter.DISABLED)
        else:
            ledPin.write(0)
            print("EXIT.")
            break
    board.exit()
    top.destroy()
    
def onExitButtonPress():
    flag.set(False)
    
top = tkinter.Tk()
top.minsize(200,30)
top.title("Potenciómetro")

descriptionLabel = tkinter.Label(top, text= "Pin A0")
descriptionLabel.grid(column=1,row=1)

analogReadLabel = tkinter.Label(top)
analogReadLabel.grid(column=1,row=2)

flag = tkinter.BooleanVar(top)
flag.set(True)

startButton = tkinter.Button(top, text="Leer", command=onStartButtonPress)
startButton.grid(column=1, row=3)

exitButton = tkinter.Button(top, text="Exit", command= onExitButtonPress)
exitButton.grid(column=2,row=3)

top.mainloop()

