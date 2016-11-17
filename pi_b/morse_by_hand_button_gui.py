import time
import Tkinter
import tkMessageBox
from Tkinter import *
import tkFont
import transmit_morsecode_with_diode

dit = 0.3

def main():
        root = Tk()
	root.wm_title("Morse Code Programm")

	#Font fuer Button
	fontdef = tkFont.Font(family='Helvetica',size=24,weight='bold')
	button = Button(root, text ="   M O R S E N   ", height=10, width=20,font=fontdef)
	button.pack(side=LEFT)

        #Button gedrueckt, Licht an; Button losgelassen, Licht aus
	button.bind('<ButtonPress-1>', diode_A_ON)
	button.bind('<ButtonRelease-1>',diode_A_OFF)
	
	root.mainloop()


#Licht an und Timer starten
def diode_A_ON(event):
        print("Button gedrueckt. Diode an.")
        transmit_morsecode_with_diode.lichtAN()
        start_time()


#Licht aus, Timer stoppen
def diode_A_OFF(event):
        print("Losgelassen. Diode aus.")
        stop_time()
        transmit_morsecode_with_diode.lichtAUS()

	
#Timer starten
def start_time():
        global initial
        initial = time.time()
        return initial


#Differenz-Zeit berechnen und interpretieren
def stop_time():        
        final = time.time()
        
        timepassed = final - initial;
        
        print 'Zeit gedrueckt: ' + str(round(timepassed,4)) + ' Sekunden'
   
        #Anzeigen, was gesendet wurde
        #Dunkelzeiten werden nicht interpretiert (# und / werden nicht angezeigt)
        if 0 < timepassed <= dit*1.5:
                print 'Interpretiere: \033[1;32m. gesendet\033[1;m'
        elif timepassed > dit*1.5:
                print 'Interpretiere: \033[1;32m- gesendet\033[1;m'

        print '\n'

	
if __name__ == "__main__":
	main()
