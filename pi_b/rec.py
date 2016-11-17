import time
import RPi.GPIO as GPIO
import config_pins

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(config_pins.pin_empfangen, GPIO.IN)

dit = 0.3

initial_lichttimer_start = False
initial_dunkeltimer_start = False
initial_letzte_zeichen_timer = False


def main():
        empfange_paket()


def empfange_paket():
        empfangsstring = ''

        #Wechsel von Hell auf Dunkel oder Dunkel auf Hell
        change = False
        ersteZeichenSchonEmpfangen = False
        letzteZeichenDesPakets = True

        anzeige_empfangsstring_zum_schluss = True

        letzte_zeichen_timer_start()
        
        while(True):
                input_value = GPIO.input(config_pins.pin_empfangen)

                #Licht von A ist an
                if input_value == 1 and change == False:
                        #Licht geht an, es ist also nicht das letzte Zeichen
                        letzteZeichenDesPakets = False

                        #Lichtzeit messen
                        lichttimer_start()

                        #ist es das erste Zeichen des Pakets?
                        #ersteZeichenSchonEmpfangen = licht ging schon einmal an, d.h. Uebertragung hat begonnen,
                        #sonst waere das erste Zeichen immer ein '#' oder '/', da ja zu Beginn das Licht aus war und
                        #der Dunkeltimer schon lief

                        if ersteZeichenSchonEmpfangen == False:
                                change = True
                                ersteZeichenSchonEmpfangen = True
                        else:
                                zeit_licht_aus = dunkeltimer_stop()
                                empfangsstring = empfangsstring + interpretiere_dunkelzeit(zeit_licht_aus)
                                change = True
                                ersteZeichenSchonEmpfangen = True
                                

                #Licht von A geht aus        
                if input_value == 0 and change == True:
                        #koennte letzte Zeichen sein
                        letzteZeichenDesPakets = True

                        #Dunkelzeit messen
                        dunkeltimer_start()

                        #Lichtzeit messen und dann im naechsten Schritt interpretieren
                        zeit_licht_an = lichttimer_stop()
                        
                        empfangsstring = empfangsstring + interpretiere_lichtzeit(zeit_licht_an)

                        change = False

                        if (len(empfangsstring) > 0 and letzteZeichenDesPakets == True):
                                letzte_zeichen_timer_start()


                #ist es das letzte Zeichen des Pakets?
                if letzteZeichenDesPakets == True and len(empfangsstring) > 0 and letzte_zeichen_timer_stop() > 15*dit:
                        if anzeige_empfangsstring_zum_schluss == True:
                                print '\033[1;34m\nEmpfangener Text:\033[1;m ' + empfangsstring

                        anzeige_empfangsstring_zum_schluss = False

                        #While-Schleife verlassen, wenn nichts mehr kommt
                        break

                
                #Wenn nach 4 Sekunden nichts kommt, ist das "Paket" (auch wenn es leer ist) abgeschlossen                
                if letzte_zeichen_timer_stop() > 15*dit:
                        #Schleife verlassen
                        break
                
        return empfangsstring


def lichttimer_start():
        #print 'Lichttimer AN'
        global initial_lichttimer_start
        initial_lichttimer_start = time.time()
        return initial_lichttimer_start


def lichttimer_stop():
        #print 'Lichttimer AUS'
        final_lichttimer_stop = time.time()
        timepassed_lichttimer = final_lichttimer_stop - initial_lichttimer_start;
        return timepassed_lichttimer
   

def dunkeltimer_start():
        #print 'Dunkeltimer AN'
        global initial_dunkeltimer_start
        initial_dunkeltimer_start = time.time()
        return initial_dunkeltimer_start


def dunkeltimer_stop():
        #print 'Dunkeltimer AUS'
        final_dunkeltimer_stop = time.time()
        timepassed_dunkeltimer = final_dunkeltimer_stop - initial_dunkeltimer_start;
        return timepassed_dunkeltimer


#misst, ob das zuletzt empfangene Zeichen das letzte des Pakets sein koennte
def letzte_zeichen_timer_start():
        print 'horche...'
        global initial_letzte_zeichen_timer
        initial_letzte_zeichen_timer = time.time()
        return initial_letzte_zeichen_timer


def letzte_zeichen_timer_stop():
        #print 'Letzte Zeichen Timer AUS'
        final_letzte_zeichen_timer_stop = time.time()
        timepassed_letzte_zeichen_time = final_letzte_zeichen_timer_stop - initial_letzte_zeichen_timer;
        return timepassed_letzte_zeichen_time


def interpretiere_lichtzeit(timepassed_licht):
        print '\nLichtzeit: ' + str(round(timepassed_licht,4)) + ' Sekunden'

        #Interpretiere die Zeit, in der die LED geleuchtet hat
        if 0 < timepassed_licht <= dit*1.5:
                print 'Interpretiere: \033[1;34m.\033[1;m'
                return '.'

        elif dit*1.5 < timepassed_licht <= 3.5*dit:
                print 'Interpretiere: \033[1;34m-\033[1;m'
                return  '-'

        else:
                print 'Interpretiere: \033[1;34m-\033[1;m'
                return '-'


def interpretiere_dunkelzeit(timepassed_dunkel):
        print '\nDunkelzeit: ' + str(round(timepassed_dunkel,4)) + ' Sekunden'

        global empfangsstring
        
        #interpreitere die Zeit, in der die LED aus war
        if 0 < timepassed_dunkel <= 4*dit:
                print 'Interpretiere:  \033[1;34m_neues Zeichen_\033[1;m'
                return ''
                
        elif 4*dit < timepassed_dunkel <= 6.5*dit: 
                print 'Interpretiere: \033[1;34m#\033[1;m'                
                return '#'
                       
        elif 6.5*dit < timepassed_dunkel <= 20*dit:
                print 'Interpretiere: \033[1;34m/\033[1;m'                
                return '/'

        else:
                print 'Interpretiere: \033[1;34m/\033[1;m'                
                return '/'

	
if __name__ == "__main__":
	main()

