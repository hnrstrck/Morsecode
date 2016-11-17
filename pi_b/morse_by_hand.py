import morse_by_hand_button_gui

def main():
	print '\033c\033[1;32mVon Hand morsen\033[0m'
	print 'LED leuchtet so lange der Button gedrueckt ist.'

	print '\n'

        #Button anzeigen (klappt nicht ueber SSH)
	morse_by_hand_button_gui.main()

	
if __name__ == "__main__":
	main()
