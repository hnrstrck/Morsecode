import rec
import morsecode_to_human_readable

def main():
        print '\033c\033[1;34mEmpfangsmodus fuers manuelle morsen\033[1;m'
        print '\n'
        
        #10 Empfangsversuche starten
        for i in range(10):
                print '\n\033[1;34mEmpfangsversuch ' + str(i+1) + '/10\033[1;m'

                #empfang
                empfangsstring = rec.empfange_paket()

                print '\033[1;34mEmpfangener Text:\033[1;m ' + empfangsstring

                #Moeglichkeit zur Uebersetzung anbieten, falls etwas empfangen wurde
                if empfangsstring != '':
                        morsecode_to_human_readable.translate_to_human_readable(empfangsstring)

	
if __name__ == "__main__":
	main()
