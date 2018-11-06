import sys
from Enigma import Enigma

while True:
    print '\n' * 40
    # Enigma(right rotor number, right rotor setting, right rotor offset, middle rotor number, ...., optional 10 pairs to plugboard)
    enigma = Enigma(4, 6, 9, 2, 8, 4, 1, 3, 19, [('A', 'T'), ('C', 'E'), ('R', 'L')])  # enigma machine creation
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
                encryptedMessage += enigma.encryptLetter(letter)
            print "Encrypted Message:",encryptedMessage

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




