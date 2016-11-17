import math
import time
import human_readable_to_morsecode
import transmit_morsecode_with_diode
import logic_protocol_send
import morsecode_to_human_readable

#Was soll bei den ersten Zeichen als 0 und was als 1 interpretiert werden?
BinaryToMC = {
'0': '-',
'1': '.'
}


#Liste mit den Paketen, zu Beginn natuerlich leer
packagesSendingList = []


def morseCodeToPackages(msg):
    msg_laenge = len(msg)
    
    print '\nPakete:'
    
    for currentNumber in xrange(1,8):

        #max 7 Pakete bauen

        #Binaerzahl erstellen
        currentNumberBinary = bin(currentNumber)
        currentNumberBinary = currentNumberBinary[2:len(currentNumberBinary)]
        currentNumberBinary = currentNumberBinary.zfill(3)

        binaryinmc = ''
       
        for char in currentNumberBinary:
            binaryinmc = binaryinmc + str(BinaryToMC[char.upper()])
            
	#Konkateniere an currentPackage zunaechst die Binaerzahl, dann die Daten in der Schleife
        currentPackage = binaryinmc

        #es muessen noch Zeichen des Morsecode-Strings (msg) in Pakete eingefuegt werden
        if len(msg) != 0:
            zeichen_passt_noch = True

            #solange ein komplettes Zeichen noch ins Paket passt
            while(zeichen_passt_noch == True):

                #Ueberpruefen, ob noch ein Zeichen bis zum naechsten # oder / rein passt
                #wird kein / gefunden, kriegt man -1 zurueck, daher muss > 0 geprueft werden
                #ein # ist immer drin (letzte Zeichen in msg)
                if len(currentPackage) + len(msg[0:msg.find('#')+1]) < 28 or (msg.find('/') > 0 and len(currentPackage) + len(msg[0:msg.find('/')+1]) < 28):

                    #ist # oder / das naechste Trennzeichen?
                    #Umbruch bei # oder / erzeugen
                    if (msg.find('/') > 0 and msg.find('#') > msg.find('/')):
                        currentPackage = currentPackage + msg[0:msg.find('/')+1]
                        msg = msg[msg.find('/')+1:msg_laenge]

                    else:
                        currentPackage = currentPackage + msg[0:msg.find('#')+1]
                        msg = msg[msg.find('#')+1:msg_laenge]

                    #Keine Leeren Pakete am Ende zulassen, daher Escape der Schleife
                    if len(msg) == 0:
                        zeichen_passt_noch = False
                                    
                else:
                    #kein Zeichen mehr Plat, brich While-Schleife ab
                    zeichen_passt_noch = False

            #Pruefziffer anhaengen
            currentPackage = currentPackage + berechne_pz(currentPackage)

            #Pakete anzeigen
            print '   PAKET ' + str(currentNumber) + ': ' + currentPackage

            #Paket in Liste einfuefen
            packagesSendingList.append(currentPackage)

        
    #falls noch etwas vom Morsecode uebrig ist, 7 Pakete aber schon voll sind
    if len(msg) > 0:
        print '\n\033[1;31mZu viele Pakete. Nur 7 gebildet.\033[1;m'
        print 'Der Teil'
        print msg + ','
        print 'uebersetzt'
        print morsecode_to_human_readable.translateMorseCodeToHumanReadable(msg) + ','
        print 'fehlt und konnte nicht in Pakete eingeteilt werden.'

    #Anzahl der Pakete anzeigen
    print '\nAnzahl Pakete:'
    print str(len(packagesSendingList))

    #am Ende:                                     
    #Liste an die Logik weitergeben zum Senden   
    logic_protocol_send.senden(packagesSendingList)


#Pruefziffer berechnen anhand des Vorkommens der Punkte im kompletten Paketstring
#sowohl ueber die Nummer als auch ueber die Daten
def berechne_pz(msg_string):
    gerade_ungerade = msg_string.count('.') % 2
            
    if gerade_ungerade == 1:
        #print 'ungerade'
        return '.'
    
    else:
        #print 'gerade'
        return '-'                                          
                                    

