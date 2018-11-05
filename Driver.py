from Enigma import Enigma

def encryptLetter():
    while True:
        letter = raw_input("Enter Letter: ")
        encryptedLetter = enigma.encryptLetter(letter)
        print "encrypted letter: "
        print encryptedLetter

def encryptMessage():
    message = raw_input("Enter Message: ")
    for letter in message:
        print encryptLetter(letter)

enigma = Enigma(0, 0, 0, 1, 0, 0, 2, 0, 0, [('A', 'C')])
input = raw_input("Encrypt A Full Message Enter-0 \ Encrypt A Single Letter-1: ")
if input == 0:
    encryptMessage()
elif input == 1:
    encryptLetter()



