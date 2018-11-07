import sys
from Enigma import Enigma
import cProfile

while True:
    print '\n' * 40

    # profiling to the while loop
    profile = cProfile.Profile()
    profile.enable()

    # enigma machine creation
    enigma = Enigma(4, 24, 18, # right rotor, setting, offset
                    5, 9, 15,  # middle rotor, setting, offset
                    2, 19, 4,  # left rotor, setting, offset
                    [('Z','U'),('H','L'),('C','Q'),('W','M'),('O','A'),('P','Y'),('E','B'),('T','R'),('D','N'),('V','I')])  # optional 10 pairs to plugboard

    # user interface handling
    input = raw_input("Enigma M3 Machine\n"
                      "=================\n"
                      "To Encrypt Full Message Enter-M\n"
                      "To Encrypt Single Letter Enter-L\n"
                      "To Exit Enter-E\n"
                      "-->:")
    if input == 'M':  # char M for message encryption
        print '\n' * 40
        while True:
            message = raw_input("\nTo Go Back Enter-1\n"
                                "Enter Message: ")
            if message == "1":
                break

            encryptedMessage = ''
            for letter in message:
                if letter == ' ':
                    encryptedMessage += ' '
                    continue
                encryptedMessage += enigma.encryptLetter(letter)
            print "Encrypted Message:", encryptedMessage

    elif input == 'L':  # char L for letter encryption
        print '\n'*40
        while True:
            letter = raw_input("\nTo Go Back Enter-1\n"
                               "Enter Letter:")
            if letter == "1":
                break

            encryptedLetter = enigma.encryptLetter(letter)
            print "encrypted letter:", encryptedLetter

    elif input == 'E':  # char E for exit from the program
        sys.exit(0)

    profile.disable()
    print '\n' * 40
    profile.print_stats(sort='time') # print the profile result
    break



