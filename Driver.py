import sys
from Enigma import Enigma
import cProfile

# profiling to the while loop
profile = cProfile.Profile()
profile.enable()

while True:
    # enigma machine creation
    enigma = Enigma(1, 0, 0,  # right rotor, setting, offset
                    2, 0, 0,  # middle rotor, setting, offset
                    3, 0, 0,  # left rotor, setting, offset
                    [('A', 'G')])  # optional 10 pairs to plugboard

    # user interface handling
    print '\n' * 3
    message = raw_input("Enigma M3 Machine (To Exit Enter-1)\n"
                        "=================\n"
                        "Enter Message:")
    if message == '1':  # char 1 for exit from the program
        break

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
sys.exit(0)




