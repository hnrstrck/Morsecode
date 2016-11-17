#!/usr/bin/envpython3
import time, RPi.GPIO as GPIO
import config_pins_abstand
    
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

#Pi A
GPIO.setup(config_pins_abstand.pin_A_senden, GPIO.OUT)      #A Diode
GPIO.setup(config_pins_abstand.pin_A_empfangen, GPIO.IN)    #A empfangen

#Pi B
GPIO.setup(config_pins_abstand.pin_B_senden, GPIO.OUT)      #B Diode
GPIO.setup(config_pins_abstand.pin_B_empfangen, GPIO.IN)    #B empfangen

#Methoden AN / AUS
def lichtAN_A():
    GPIO.output(config_pins_abstand.pin_A_senden, True)


def lichtAUS_A():
    GPIO.output(config_pins_abstand.pin_A_senden, False)


def lichtAN_B():
    GPIO.output(config_pins_abstand.pin_B_senden, True)


def lichtAUS_B():
    GPIO.output(config_pins_abstand.pin_B_senden, False)
    
def blinken():
    lichtAUS_A()
    lichtAN_A()
    time.sleep(0.5)
    lichtAUS_A()
    time.sleep(0.5)
    lichtAN_A()
    time.sleep(0.5)
    lichtAUS_A()
    time.sleep(0.5)
    lichtAN_A()
    time.sleep(0.5)
    lichtAUS_A()
    time.sleep(0.5)
    
    lichtAUS_B()
    lichtAN_B()
    time.sleep(0.5)
    lichtAUS_B()
    time.sleep(0.5)
    lichtAN_B()
    time.sleep(0.5)
    lichtAUS_B()
    time.sleep(0.5)
    lichtAN_B()
    time.sleep(0.5)
    lichtAUS_B()
    
def main():
    #zaehler fuer positive Ergebnisse
    pos_test_A = 0
    pos_test_B = 0
    
    # alle Lichter aus zu Beginn
    lichtAUS_A()
    lichtAUS_B()

    print('\033cAchtung!\n\n')

    blinken()


    #Teste Empfang von B
    print('Test gestartet\n\n')


    time.sleep(2)

    print('Teste Empfang von B (Diode von A an)')

    lichtAN_A()

    i = 1

    time.sleep(0.5)
    while i<=25:
        input_value_B = GPIO.input(config_pins_abstand.pin_B_empfangen)

        if input_value_B == 1:
            print('B empfaengt etwas - Nr. ' + str(i) + ' / 25')
            i = i+1
            pos_test_B = pos_test_B + 1
        else:
            print('!!! - kein Empfang von B - Nr. ' + str(i) + ' / 25')
            i = i+1
            
        time.sleep(0.2)

    lichtAUS_A()

    print('\n')
    
    time.sleep(1)

    print('Teste Empfang von A (Diode von B an)')

    lichtAN_B()
    
    i = 1

    time.sleep(0.5)
    while i<=25:
        input_value_A = GPIO.input(config_pins_abstand.pin_A_empfangen)

        if input_value_A == 1:
            print('A empfaengt etwas - Nr. ' + str(i) + ' / 25')
            i = i+1
            pos_test_A = pos_test_A + 1
        else:
            print('!!! - kein Empfang von A - Nr. ' + str(i) + ' / 25')
            i = i+1
        
        time.sleep(0.2)

    lichtAUS_B()
        
    print(' \n')
    
    #time.sleep(2)

    print('Test abgeschlossen\n')
    print('Ergebnis:')
    print('Empfang von B: ' + str(pos_test_B) + ' / 25 erfolgreich')
    print('Empfang von A: ' + str(pos_test_A) + ' / 25 erfolgreich')
 
if __name__ == "__main__":
    main()
