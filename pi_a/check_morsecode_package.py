def return_number(paketstring):
        position = 0

        binzahl = [0,0,0]

        #die ersten drei Zeichen im Paket stehen fuer die Nummer des Pakets
        #bspw. --. = 001
        if paketstring[0:1] is '-':
                binzahl[0] = 0
        else:
                binzahl[0] = 1

        if paketstring[1:2] is '-':
                binzahl[1] = 0
        else:
                binzahl[1] = 1

        if paketstring[2:3] is '-':
                binzahl[2] = 0
        else:
                binzahl[2] = 1

        #Umrechnung
        position = (int(binzahl[0]) * 4) + (int(binzahl[1])*2) + int(binzahl[2])

        return position


def return_daten(paketstring):
        #Daten ab dem einschliesslich 4. Zeichen
        #bis einschliesslich vorletzte Zeichen
        datastring = paketstring[3:len(paketstring)-1]

        return datastring      


def package_auswerten(paketstring):
        #stimmt die Pruefziffer?
        #berechnet ueber inkl. Positionsnummer und Datenstring
        anzahl_dots_in_data_and_pos = paketstring[0:len(paketstring)-1].count('.') 

        pruefziffer = ''

        #gerade: -
        #ungerade: .
        if anzahl_dots_in_data_and_pos % 2 == 1:
            pruefziffer = '.'
        else: 
            pruefziffer = '-'

        print 'Pruefziffer errechnet: ' + pruefziffer
        print 'Pruefziffer Paket:     ' + paketstring[len(paketstring)-1]
        print 'Daten:                 ' + return_daten(paketstring)

        if pruefziffer is paketstring[len(paketstring)-1]:       
            print 'Position vom Paket:    ' + str(return_number(paketstring))
            print 'Paket \033[1;32mOKAY\033[1;m'

            return True
        else:
            print '\033[1;31mError im Paket\033[1;m'
            
            return False 
 	
