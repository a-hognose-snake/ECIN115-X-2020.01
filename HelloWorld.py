#   Se declara uso de la libreria
import tkinter
#   Declaracion de uso de firmata
from pyfirmata2 import Arduino
#   Se utilizara la funcion sleep de la libreria time
from time import sleep

def HelloWorld():
    #   Se declara una raiz/ventana
    top = tkinter.Tk()
    #   Se declara el nombre de la ventana
    top.title("Hello GUI")
    #   Se declaran las dimensiones minimas de la ventana
    top.minsize(200,30)
    #   Ubicacion de texto y texto
    hellolabel = tkinter.Label(top, text = "Hello World")
    #   Hace visible la ventana
    hellolabel.pack()
    #   Realiza la permanencia de la accion declarada, 
    #   hasta que se cierra la ventana
    top.mainloop()
    
HelloWorld()

