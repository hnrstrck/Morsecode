#!/usr/bin/envpython3

import morse_by_hand
import morse_by_commandline
import logic_protocol_rec
import logic_by_hand_rec
import led_off

def main():
        #LED ausmachen, wenn Programm bspw. abgestuerzt ist oder mit CTRL+C abgebrochen wurde
        #Dann koennte die LED noch leuchten
        led_off.main()

        
        #\033c loescht das Terminal
        #\033[1;31m und andere aktiviert Farben, \033[1;1m deaktiviert Farben wieder
	print '\033c\033[1;33mMORSE CODE PROGRAMM\033[1;m'
        print '\033[1;31m*******************\033[1;m\n'
	print 'Was moechten Sie?'
	print '[1]      \033[1;32msenden\033[0m: komfortabel Text von der Kommandozeile morsen (mit Protokoll)'
	print '[2]      \033[1;32msenden\033[0m: von Hand morsen'
	print '[3]      \033[1;34mempfangen\033[0m: Empfangsmodus fuer das Protokoll aktivieren'
	print '[4]      \033[1;34mempfangen\033[0m: Empfangsmodus fuer das manuelle Morsen aktivieren'

	auswahl = raw_input('Auswahl [1..4]: ')

        #Weiterleiten
	if auswahl is '1':
		morse_by_commandline.main()
	elif auswahl is '2':
		morse_by_hand.main()
	elif auswahl is '3':
		logic_protocol_rec.main()
        elif auswahl is '4':
                logic_by_hand_rec.main()
	else:
		main()

		
if __name__ == "__main__":
	main()
