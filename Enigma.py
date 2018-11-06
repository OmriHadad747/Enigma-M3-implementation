from Plugboard import Plugboard
from Reflector import Reflector
from Rotor import Rotor

class Enigma:

    def __init__(self, rRotor, rSetting, rOffset, mRotor, mSetting, mOffset, lRotor, lSetting, lOffset, pbConfiguration):
        self.rotors = []
        self.createRotors()

        self.rRotor = rRotor-1
        self.mRotor = mRotor-1
        self.lRotor = lRotor-1
        self.selectedRotors = []
        self.selectRotors()
        self.setRotorsSettings(rSetting, mSetting, lSetting)
        self.setRotorsOffsets(rOffset, mOffset, lOffset)

        self.reflector = self.createReflector()

        self.plugboard = Plugboard(pbConfiguration)

    def createRotors(self):
        self.rotors.append(Rotor("I", list("EKMFLGDQVZNTOWYHXUSPAIBRCJ"), "Q"))
        self.rotors.append(Rotor("II", list("AJDKSIRUXBLHWTMCQGZNPYFVOE"), "E"))
        self.rotors.append(Rotor("III", list("BDFHJLCPRTXVZNYEIWGAKMUSQO"), "V"))
        self.rotors.append(Rotor("IV", list("ESOVPZJAYQUIRHXLNFTGKDCMWB"), "J"))
        self.rotors.append(Rotor("V", list("VZBRGITYUPSDNHLXAWMJQOFECK"), "Z"))

    def selectRotors(self):
        self.selectedRotors.append(self.rotors[self.rRotor])
        self.rRotor = 0
        self.selectedRotors.append(self.rotors[self.mRotor])
        self.mRotor = 1
        self.selectedRotors.append(self.rotors[self.lRotor])
        self.lRotor = 2

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

    def changeDir(self):
        self.selectedRotors[self.rRotor].changeDirection()
        self.selectedRotors[self.mRotor].changeDirection()
        self.selectedRotors[self.lRotor].changeDirection()

    def encryptLetter(self, letter):
        # turnover and double step mechanism
        if self.selectedRotors[self.rRotor].isTurnover() or self.selectedRotors[self.mRotor].isTurnover():
            if self.selectedRotors[self.mRotor].isTurnover():
                self.selectedRotors[self.lRotor].step()

            self.selectedRotors[self.mRotor].step()

        self.selectedRotors[self.rRotor].step()

        # forward direction translation
        letter = self.plugboard.translation(letter)
        letter = self.selectedRotors[self.rRotor].translation(letter)
        letter = self.selectedRotors[self.mRotor].translation(letter)
        letter = self.selectedRotors[self.lRotor].translation(letter)
        letter = self.reflector.translation(letter)

        self.changeDir()

        # reverse direction translation
        letter = self.selectedRotors[self.lRotor].translation(letter)
        letter = self.selectedRotors[self.mRotor].translation(letter)
        letter = self.selectedRotors[self.rRotor].translation(letter)
        letter = self.plugboard.translation(letter)

        self.changeDir()

        return letter