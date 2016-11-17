import human_readable_to_morsecode

def main():
	eingabetext = raw_input('Bitte geben Sie Text ein:\n')
        
        #Text uebersetzen in MC (weiterleiten)
        human_readable_to_morsecode.translateHumanReadableToMorseCode(eingabetext)


if __name__ == "__main__":
	main()
