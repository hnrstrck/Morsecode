import morsecode_to_packages
import morsecode_to_human_readable
import re #fuer String-Operationen

HumanReadableCharacterToMorseCodeCharakter = {
'A': '.-',
'B': '-...',
'C': '-.-.',
'D': '-..',
'E': '.',
'F': '..-.',
'G': '--.',
'H': '....',
'I': '..',
'J': '.---',
'K': '-.-',
'L': '.-..',
'M': '--',
'N': '-.',
'O': '---',
'P': '.--.',
'Q': '--.-',
'R': '.-.',
'S': '...',
'T': '-',
'U': '..-',
'V': '...-',
'W': '.--',
'X': '-..-',
'Y': '-.--',
'Z': '--..',

'0': '-----',
'1': '.----',
'2': '..---',
'3': '...--',
'4': '....-',
'5': '.....',
'6': '-....',
'7': '--...',
'8': '---..',
'9': '----.',

'.':'.-.-.-',
',':'--..--',
':':'---...',
'?':'..--..',
"'":'.----.',
'-':'-....-',
'/':'-..-.',
'@': '.--.-.',
'=':'-...-',
'(':'-.--.',
')':'-.--.-',
'+':'.-.-.'
}


def translateHumanReadableToMorseCode(msg):
	morsecode_complete = ''

	change = False

        #entferne doppelte / mehrfache Leerzeichen
        if len(re.sub(' +', ' ', msg)) != len(msg):
                print '\033[1;035m\nMehrfache Leerzeichen enfernt.\033[1;m'
                msg = re.sub(' +', ' ', msg)
                change = True
                
        #entferne evtl. Leerzeichen zu Beginn
	if msg[0] is ' ':	
		print '\033[1;035m\nErstes Zeichen war ein Leerzeichen - wurde enfernt.\033[1;m'
		msg = msg[1:len(msg)]
		change = True

	#entferne evtl. Leerzeichen am Ende
	if msg[len(msg)-1:len(msg)] is ' ':	
		print '\033[1;035m\nLetztes Zeichen war ein Leerzeichen - wurde enfernt.\033[1;m'
		msg = msg[0:len(msg)-1]
		change = True

        #anzeigen, falls String geaendert wurde
        if change == True:
                print '\nVeraenderter String:'
                print msg

        #Uebersetzen falls moeglich
	try:
		for char in msg:
			if char is not ' ':	
				morsecode_complete = morsecode_complete + str(HumanReadableCharacterToMorseCodeCharakter[char.upper()]) + "#"
			if char is ' ':
				#entferne bei Leerzeichen das letzte Zeichen (ist ein '#'), damit kein '#/' vorkommt und haenge '/' an
				morsecode_complete = morsecode_complete[0:len(morsecode_complete)-1]
				morsecode_complete = morsecode_complete + "/"
				
	except:
                #Umlaute und Anfuehrungszeichen bspw. koennen nicht uebersetzt werden
		print '\033[1;31m\nFehler bei der Umwandlung in Morse-Code.\033[1;m'
                print 'Zeichen ' + char + ' kann nicht uebersetzt werden.'
                print 'Der Text wird bis zum problematischen Zeichen uebersetzt.'
                #Anzeigen, was soweit uebersetzt werden konnte (MC->HR zurueck)
                print morsecode_to_human_readable.translateMorseCodeToHumanReadable(morsecode_complete)
	else:
                #alles konnte uebersetzt werden
		print '\033[1;32m\nKeine Fehler bei der Umwandlung in Morse-Code.\033[1;m'

        #Zaehle Zeichen
	print '\nAnzahl zu uebertragener Zeichen:'
	print str(len(morsecode_to_human_readable.translateMorseCodeToHumanReadable(morsecode_complete)))
	
	#Zeige MC an	
	print '\nMorsecode zum Uebertragen:'
	print morsecode_complete	

	#Weiterleiten zum Einteilen in Pakete
	morsecode_to_packages.morseCodeToPackages(morsecode_complete)

