# Para comenzar a usar pyFirmata debemos 
# importar el paquete correspondiente al 
# inicio de nuestro programa
from pyfirmata2 import Arduino
import time
#creamos un objeto que representa nuestra 
# placa (board) de Arduino. Para ello 
# necesitamos indicar como cadena de
#caracteres el puerto o bien usar .AUTODETECT
arduino = Arduino(Arduino.AUTODETECT)
# Se definen los pines digitales
LED_r = 13
LED_am = 8
LED_az = 6
# Se crea un loop que se repite 1 vez que 
# genera una acción cada 1.5 segundos
for x in range(1):
    #Se prende el LED rojo primero y 
    # despues los otros sequencialmente
    arduino.digital[LED_r].write(1)
    arduino.digital[LED_am].write(0)
    arduino.digital[LED_az].write(0)
    time.sleep(1.5)
    arduino.digital[LED_r].write(1)
    arduino.digital[LED_am].write(1)
    arduino.digital[LED_az].write(0)
    time.sleep(1.5)
    arduino.digital[LED_r].write(1)
    arduino.digital[LED_am].write(1)
    arduino.digital[LED_az].write(1)
    time.sleep(1.5)
    #Se empiezan a apagar secuencialmente los LEDs
    arduino.digital[LED_r].write(1)
    arduino.digital[LED_am].write(1)
    arduino.digital[LED_az].write(0)
    time.sleep(1.5)
    arduino.digital[LED_r].write(1)
    arduino.digital[LED_am].write(0)
    arduino.digital[LED_az].write(0)
    time.sleep(1.5)
    arduino.digital[LED_r].write(0)
    arduino.digital[LED_am].write(0)
    arduino.digital[LED_az].write(0)
    time.sleep(1.5)
#Por último, para terminar nuestro programa 
# de manera limpia, se debe invocar el método exit()
arduino.exit()
