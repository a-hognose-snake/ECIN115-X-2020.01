from pyfirmata2 import Arduino,util
import tkinter


def onStartButtonPress():
    while True:
        if flag.get():
            analogReadLabel.config(text=str(a0.read()))
            analogReadLabel.update_idletasks()
            top.update()
        else:
            break
    board.exit()
    top.destroy()
    
def onExitButtonPress():
    flag.set(False)
    
board = Arduino('/dev/cu.usbmodem14201')

it = util.Iterator(board)
it.start()

a0 = board.get_pin('a:0:i')

ledPin = board.get_pin('d:11:p')


top = tkinter.Tk()
top.title("Potenciómetro")

descriptionLabel = tkinter.Label(top, text= "Leer")
descriptionLabel.grid(column=1,row=1)

analogReadLabel = tkinter.Label(top, text= "Apreta Start...")
analogReadLabel.grid(column=2,row=1)

flag = tkinter.BooleanVar(top)
flag.set(True)

startButton = tkinter.Button(top, text="Start", command=onStartButtonPress)
startButton.grid(column=1, row=2)

exitButton = tkinter.Button(top, text="Exit", command= onExitButtonPress)
exitButton.grid(column=2,row=2)

top.mainloop()

