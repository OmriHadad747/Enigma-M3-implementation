from Plugboard import Plugboard
from Reflector import Reflector
from Rotor import Rotor


class Enigma:

    def __init__(self, rRotor, rSetting, rOffset,
                       mRotor, mSetting, mOffset,
                       lRotor, lSetting, lOffset,
                       pbConfiguration):
        self.rotors = []
        self.createRotors()

        self.rRotor = None
        self.mRotor = None
        self.lRotor = None
        self.selectRotors(rRotor - 1, mRotor - 1, lRotor - 1)
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

    def selectRotors(self, rRotor, mRotor, lRotor):
        self.rRotor = self.rotors[rRotor]
        self.mRotor = self.rotors[mRotor]
        self.lRotor = self.rotors[lRotor]

    def setRotorsSettings(self, rSetting, mSetting, lSetting):
        self.rRotor.setSetting(rSetting)
        self.mRotor.setSetting(mSetting)
        self.lRotor.setSetting(lSetting)

    def setRotorsOffsets(self, rOffset, mOffset, lOffset):
        self.rRotor.setOffset(rOffset)
        self.mRotor.setOffset(mOffset)
        self.lRotor.setOffset(lOffset)

    @staticmethod
    def createReflector():
        return Reflector(list("YRUHQSLDPXNGOKMIEBFZCWVJAT"))

    def changeDir(self):
        self.rRotor.changeDirection()
        self.mRotor.changeDirection()
        self.lRotor.changeDirection()

    def encryptLetter(self, letter):
        # turnover and double step mechanism
        if self.rRotor.isTurnover() or self.mRotor.isTurnover():
            if self.mRotor.isTurnover():
                self.lRotor.step()

            self.mRotor.step()

        self.rRotor.step()

        # forward direction translation
        letter = self.plugboard.translation(letter)
        letter = self.rRotor.translation(letter)
        letter = self.mRotor.translation(letter)
        letter = self.lRotor.translation(letter)
        letter = self.reflector.translation(letter)

        self.changeDir()

        # reverse direction translation
        letter = self.lRotor.translation(letter)
        letter = self.mRotor.translation(letter)
        letter = self.rRotor.translation(letter)
        letter = self.plugboard.translation(letter)

        self.changeDir()

        return letter