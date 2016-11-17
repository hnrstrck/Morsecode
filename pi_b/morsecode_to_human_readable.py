MorseCodeCharacterToHumanReadableCharacter = {
'.-':'A',
'-...':'B',
 '-.-.':'C',
'-..':'D' ,
'.':'E' ,
'..-.'  :'F' ,
'--.':'G' ,
'....':'H' ,
'..':'I' ,
'.---':'J' ,
'-.-':'K' ,
'.-..':'L' ,
'--':'M' ,
'-.':'N' ,
'---':'O' ,
'.--.':'P' ,
'--.-':'Q' ,
'.-.':'R' ,
'...':'S' ,
'-':'T' ,
'..-':'U' ,
'...-':'V' ,
'.--':'W' ,
'-..-':'X' ,
'-.--':'Y',
'--..':'Z',

'-----':'0',
'.----':'1',
'..---':'2',
'...--':'3',
'....-':'4',
'.....':'4',
'-....':'6',
'--...':'7',
'---..':'8',
'----.':'9',

'.-.-.-':'.',
'--..--':',',
'---...':':',
'..--..':'?',
'.----.':"'",
'-....-':'-',
'-..-.':'/',
'.--.-.':'@',
'-...-':'=',
'-.--.':'(',
'-.--.-':')',
'.-.-.':'+',
}


#fuer Strings inkl. Abfrage
def translate_to_human_readable(empfangsstring):
    print '\nSoll der String'
    print empfangsstring
    print 'uebersetzt werden?'
    print '[1]	Uebersetzen'
    print '[2]	Abbrechen'

    auswahl = raw_input('Auswahl [1 / 2]: ')

    if auswahl is '1':

        #String uebersetzten (mit Methode unten)
	uebersetzung = translateMorseCodeToHumanReadable(empfangsstring)	
        print '\nMorse-Code:   ' + empfangsstring
        print 'Uebersetzung: ' + uebersetzung
        print '\033[1;31m\nEnde.\033[1;m'

    elif auswahl is '2':
	print '\033[1;31m\nAbbruch.\033[1;m'

    else:
	translate_to_human_readable(empfangsstring)


#fuer Strings ohne Abfrage
def translateMorseCodeToHumanReadable(msg):
    humanReadableText = ''

    #Am Ende vom String muss ein '#' sein (als Trenner fuer die Uebersetzung)
    #sonst anhaengen
    if msg[len(msg):len(msg)+1] != '#':
        msg = msg + '#'
        
    #Uebersetzte alles    
    while msg != '':
        positionSlash = msg.find('/')
        positionRaute = msg.find('#')

        #Substrings bis zum naechsten / bzw. # finden und uebersetzten (s. Array oben)
        if positionSlash < positionRaute and positionSlash > 0:
            try:
                humanReadableText = humanReadableText + str(MorseCodeCharacterToHumanReadableCharacter[msg[0:positionSlash ]]) + ' '
            except:
                pass
                
            #Uebersetzten Morsecode von Beginn entfernen
            msg = msg[positionSlash+1:len(msg)+1]
            
        else:
            try:
                humanReadableText = humanReadableText + str(MorseCodeCharacterToHumanReadableCharacter[msg[0:positionRaute]])
            except:
                pass

            #Uebersetzten Morsecode von Beginn entfernen
            msg = msg[positionRaute+1:len(msg)+1]
            
    return humanReadableText

