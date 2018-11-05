from Plugboard import Plugboard
from Reflector import Reflector
from Rotor import Rotor

class Enigma:

    def __init__(self, rRotor, rSetting, rOffset, mRotor, mSetting, mOffset, lRotor, lSetting, lOffset, pbConfiguration):
        self.rotors = []
        self.createRotors()

        self.rRotor = rRotor
        self.mRotor = mRotor
        self.lRotor = lRotor
        self.selectedRotors = []
        self.selectRotors()
        self.setRotorsSettings(rSetting, mSetting, lSetting)
        self.setRotorsOffsets(rOffset, mOffset, lOffset)

        self.reflector = self.createReflector()

        self.plugboard = Plugboard(pbConfiguration)

    def createRotors(self):
        self.rotors.append(Rotor("I", list("EKMFLGDQVZNTOWYHXUSPAIBRCJ"), "Q"))
        self.rotors.append(Rotor("II",list("AJDKSIRUXBLHWTMCQGZNPYFVOE"), "E"))
        self.rotors.append(Rotor("III", list("BDFHJLCPRTXVZNYEIWGAKMUSQO"), "V"))
        self.rotors.append(Rotor("IV", list("ESOVPZJAYQUIRHXLNFTGKDCMWB"), "J"))
        self.rotors.append(Rotor("V", list("VZBRGITYUPSDNHLXAWMJQOFECK"), "Z"))

    def selectRotors(self):
        self.selectedRotors.append(self.rotors[self.rRotor])
        self.selectedRotors.append(self.rotors[self.mRotor])
        self.selectedRotors.append(self.rotors[self.lRotor])

    def setRotorsSettings(self, rSetting, mSetting, lSetting):
        self.selectedRotors[self.rRotor].setSetting(rSetting)
        self.selectedRotors[self.mRotor].setSetting(mSetting)
        self.selectedRotors[self.lRotor].setSetting(lSetting)

    def setRotorsOffsets(self, rOffset, mOffset, lOffset):
        self.selectedRotors[self.rRotor].setOffset(rOffset)
        self.selectedRotors[self.mRotor].setOffset(mOffset)
        self.selectedRotors[self.lRotor].setOffset(lOffset)

    @staticmethod
    def createReflector():
        return Reflector(list("YRUHQSLDPXNGOKMIEBFZCWVJAT"))

    #def encryptLetter(self, letter):

