import RPi.GPIO as GPIO
import config_pins

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(config_pins.pin_senden, GPIO.OUT)


def main():
    ledAUS()							


#Licht aus machen der Sende-LED
def ledAUS():
    GPIO.output(config_pins.pin_senden, False)

         
if __name__ == "__main__":
    main()
	
