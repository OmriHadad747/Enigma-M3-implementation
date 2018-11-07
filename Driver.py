import sys
from Enigma import Enigma
import cProfile

while True:
    # profiling to the while loop
    profile = cProfile.Profile()
    profile.enable()

    # enigma machine creation
    enigma = Enigma(4, 24, 18, # right rotor, setting, offset
                    5, 9, 15,  # middle rotor, setting, offset
                    2, 19, 4,  # left rotor, setting, offset
                    [('Z','U'),('H','L'),('C','Q'),('W','M'),('O','A'),('P','Y'),('E','B'),('T','R'),('D','N'),('V','I')])  # optional 10 pairs to plugboard

    # user interface handling
    while True:
        print '\n' * 3
        message = raw_input("Enigma M3 Machine (To Exit Enter-1)\n"
                            "=================\n"
                            "Enter Message:")
        if message == '1':  # char 1 for exit from the program
            sys.exit(0)

        encryptedMessage = ''
        for letter in message:
            if letter == ' ':
                encryptedMessage += ' '
                continue
            encryptedMessage += enigma.encryptLetter(letter)
        print "Encrypted Message:", encryptedMessage

    profile.disable()
    print '\n' * 10
    profile.print_stats(sort='time') # print the profile result
    break



