import rec
import morsecode_to_human_readable
import transmit_morsecode_with_diode
import check_morsecode_package
import time

initial_letzte_paket_time = False

def main():
        print '\033c\033[1;34mEmpfangsmodus fuers Protokoll\033[1;m\n'
        
        print '\033[1;34m\nWarte auf Anfragen\033[1;m\n'

        #3 Empfangsversuche fuer den Verbindungsaufbau
        for i in range(3):
                empfangene_pakete = empfangen()
                
                #wenn etwas empfangen wurde, break
                if len(empfangene_pakete[0]) != 0:
                        break

        #evtl. empfangene Pakete uebersetzen
        if len(empfangene_pakete[0]) != 0:
                uebersetzen(empfangene_pakete)
                
        #nichts empfangen, kein Verbindungsaufbau
        if len(empfangene_pakete[0]) == 0:
                print '\033[1;31m\nEnde durch Timeout.\033[1;m'

        
def empfangen():
        #max 7 Pakete (aufgrund der Nummerierung)
        empfangene_pakete = ['','','','','','','']
        
        verbindungsaufbau = str(rec.empfange_paket())

        if verbindungsaufbau == '-.-.-':
                print '\033[1;32m\nVerbindung etabliert\033[1;m'

        if verbindungsaufbau == '-.-.-':
                transmit_morsecode_with_diode.sende_ACK()
                print '\n\033[1;34mBereit fuer Paketempfang\033[1;m'

                #Timer starten
                #Timer dient dem Abbruch der Endlosschleife, die so lange laeuft, wie etwas empfangen wird
                #Der Timer wird bei Empfang eines Zeichens immer wieder neu gestartet
                letzte_paket_timer_start()

                while(True):
                        #empfang
                        paket = rec.empfange_paket()

                        #etwas empfangen
                        if paket is not '':
                                print '\033[1;34m\nUeberpruefe Paket: ' + paket + '\033[1;m'

                                #Ueberpruefe Pruefziffer
                                if check_morsecode_package.package_auswerten(paket) == True:
                                        #Paket OKAY --> Sende ACK
                                        transmit_morsecode_with_diode.sende_ACK()

                                        print '\n'

                                        #fuege Paket an der richtigen Stelle ins Array ein
                                        #Da nur 7 Pakete geschickt werden koennen, ist ein Array ausreichend, ansonsten mit anderer Datenstruktur arbeiten
                                        insert_pos = check_morsecode_package.return_number(paket)
                                        empfangene_pakete[insert_pos-1] = check_morsecode_package.return_daten(paket)

                                        #Timer wieder starten
                                        letzte_paket_timer_start()
                                else:
                                        #Paket nicht OKAY --> Sende NACK
                                        transmit_morsecode_with_diode.sende_NACK()

                                        print '\n'

                                        #Timer wieder starten
                                        letzte_paket_timer_start()


                        #timeout nach 15 Sekunden
                        #Es wird ca. 4 mal die Schleife ausgefuehrt, ob vielleicht doch etwas kommt.
                        #Dabei braucht der Aufruf rec.empfange_paket() eine Zeit von 15*dits = 4,5 Sekunden

                        #nichts empfangen
                        if paket is '' and letzte_paket_timer_stop() > 15:
                                print '\033[1;31m\nNichts mehr empfangen.\033[1;m'
                                print '\033[1;31m\nEnde durch Timeout.\033[1;m'
                                break

        else:
                print '\033[1;31m\nVerbindung nicht etabliert.\033[1;m'
            

        return empfangene_pakete


def uebersetzen(empfangene_pakete):
        empfangsstring = ''

        #mache aus dem Array einen String
        for i in range(len(empfangene_pakete)):
                empfangsstring = empfangsstring + str(empfangene_pakete[i])

        #String weiterleiten zur Uebersetzung
        morsecode_to_human_readable.translate_to_human_readable(empfangsstring)
 
                                
def letzte_paket_timer_start():
        global initial_letzte_paket_time
        initial_letzte_paket_time = time.time()
        return initial_letzte_paket_time


def letzte_paket_timer_stop():
        final_letzte_paket_timer_stop = time.time()
        timepassed_letzte_paket_time = final_letzte_paket_timer_stop - initial_letzte_paket_time
        return timepassed_letzte_paket_time

	
if __name__ == "__main__":
	main()
