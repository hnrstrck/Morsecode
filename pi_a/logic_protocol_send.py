import transmit_morsecode_with_diode
import morsecode_to_human_readable
import check_morsecode_package
import rec
import random

#Strings fuer ACK, NACK festlegen
ACK = '...-.'
NACK = '........'


def warte_auf_bestaetigung():
        print '\n\033[1;34mWarte auf Bestaetigung\033[1;m'
        
        bestaetigung = ''

        #3 Versuche eine Bestaetigung zu erhalten
        #Dauert so lange, wie rec.empfange_paket() laeuft
        for i in range(3):
                bestaetigung = rec.empfange_paket()
                if bestaetigung != '':
                        break
                
        if bestaetigung == '':
                print '\n\033[1;31mKeine Bestaetigung erhalten.'

        #gib empfangenen String zurueck
        return bestaetigung


def senden(packagesSendingList):
    print '\nMit dem Morsen beginnen?'
    print '[1]	Senden'
    print '[2]	Abbrechen'

    auswahl = raw_input('Auswahl [1 / 2]: ')

    if auswahl is '1':
        #Verbindungsaufbau    
        transmit_morsecode_with_diode.verbindungsaufbau()

        #warte auf bestaetigung
        verbindungsaufbau_best = warte_auf_bestaetigung()

        if verbindungsaufbau_best == ACK:
                print '\033[1;32m\nVerbindung etaliert\033[1;m'
                print '\033[1;32m\nSende nun Paket(e)\033[1;m'

                #Pakete shufflen, damit die Nummerierung genutzt werden kann auf der Empfangsseite
                random.shuffle(packagesSendingList)

                #Sende so lange, bis die Paketliste leer ist (Paket wird entfernt, wenn ein ACK zurueck kommt,
                #sonst wird das Paket erneut gesendet (kann in Endlosschleife resultieren, wenn auf der
                #Empfangsseite evtl. die Pakete falsch verifiziert / ueberprueft oder immer nur NACKs zurueck schickt.
                #Dabei wird die Paketliste von vorne bis hinten durchlaufen (Liste vorher geshuffelt)
                while(len(packagesSendingList) != 0):
                        print '\n\033[1;32mSende Paket Nr. ' + str(check_morsecode_package.return_number(packagesSendingList[0])) + '\033[1;m'

                        #Paket schicken
                        transmit_morsecode_with_diode.transmit_packagestring(packagesSendingList[0])

                        #warte auf ACK / NACK
                        bestaetigung = warte_auf_bestaetigung()

                        if bestaetigung == NACK:
                                print '\033[1;31m\nPaket nicht erfolgreich uebermittelt\033[1;m'

                                #und erneut senden bei NACK
                                pass
                        elif bestaetigung == ACK:
                                print '\033[1;32m\nPaket Nr. ' + str(check_morsecode_package.return_number(packagesSendingList[0])) + ' erfolgreich  uebermittelt\033[1;m'

                                #Senden war erfolgreich, loesche Paket
                                del packagesSendingList[0]
                        else:
                                print '\033[1;31m\nError - Empfang von Paket Nr. ' + str(check_morsecode_package.return_number(packagesSendingList[0])) + ' weder bestaetigt noch unbestaetigt\033[1;m'

                #Liste leer
                print '\033[1;32m\nPaketliste leer\033[1;m'
                print '\033[1;32m\nAlle Pakete uebertragen\033[1;m'

        #keine Verbindung etabliert
        if verbindungsaufbau_best == NACK or verbindungsaufbau_best == '': 
                print '\n\033[1;31mVerbindung konnte nicht etabliert werden.\033[1;m'
                print '\nStarte erneuten Versuch:'

                senden(packagesSendingList)

    elif auswahl is '2':
	print '\033[1;31mAbbruch.\033[1;m'

    #falsche Eingabe, erneuter Versuch
    else:
	senden(packagesSendingList)


