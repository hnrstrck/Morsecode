import time
import RPi.GPIO as GPIO
import config_pins


GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(config_pins.pin_senden, GPIO.OUT)


dit = 0.3

ACK = '...-.'
NACK = '........'
string_aufbau = '-.-.-'

def main():
    print 'Uebermittle an Diode:\n'
    verbindungsaufbau()


def verbindungsaufbau():
    print '\033[1;32m\nSENDE Verbindungsaufbau\033[1;m'
    transmit_packagestring(string_aufbau)


def sende_ACK():
    print '\033[1;32m\nSENDE ACK\033[1;m'
    transmit_packagestring(ACK)


def sende_NACK():
    print '\033[1;32m\nSENDE NACK\033[1;m'
    transmit_packagestring(NACK)


def transmit_packagestring(currPackage):
        currPackage_anzeige = currPackage
    
        for char in range(len(currPackage)):
            currPackage_anzeige = currPackage_anzeige[:char] + '[\033[1;32m' + currPackage[char] + '\033[1;m]' + currPackage_anzeige[char+1:]

            print currPackage_anzeige

            #Licht an / aus fuer das jew. Zeichen            
            if currPackage[char] is '.':	
                #print 'SENDE . AN' + ' Zeichen ' + str(char+1) + ' / ' + str(len(currPackage))
		lichtAN()
		time.sleep(dit)
		lichtAUS()
		#print '        AUS'
				
	    if currPackage[char] is '-':
		#print 'SENDE - AN' + ' Zeichen ' + str(char+1) + ' / ' + str(len(currPackage))
		lichtAN()
		time.sleep(3*dit)
		lichtAUS()
		#print '        AUS'
		
	    if currPackage[char] is '#':
		#print 'SENDE # WARTE' + ' Zeichen ' + str(char+1) + ' / ' + str(len(currPackage))
		time.sleep(3*dit)
		#print '        WARTE ENDE'
			
	    if currPackage[char] is '/':
		#print 'SENDE / WARTE' + ' Zeichen ' + str(char+1) + ' / ' + str(len(currPackage))
		time.sleep(7*dit)
		#print '        WARTE ENDE'

	    #Trennung zwischen zwei Zeichen im MC-Package
	    #Dunkelzeit von einem dit zw. den Zeichen in MC
	    if char<len(currPackage)-1:
                if currPackage[char+1] is '.' or '-':
                    time.sleep(dit)
			
            #Entfernen von '[' und ']' inkl. Farbe
            currPackage_anzeige = currPackage_anzeige.replace('\033[1;m]','')
            currPackage_anzeige = currPackage_anzeige.replace('[\033[1;32m','')
							

def lichtAN():
    GPIO.output(config_pins.pin_senden, True)

    
def lichtAUS():
    GPIO.output(config_pins.pin_senden, False)

         
if __name__ == "__main__":
    main()
	
