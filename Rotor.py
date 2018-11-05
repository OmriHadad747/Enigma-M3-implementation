from Translator import Translator



class Rotor(Translator):

    SIZE = 25
    permutation = []
    reversePermutation = [SIZE]

    def __init__(self, name, permutation, turnOver):
        self.name = name
        self.permutation = permutation
        self.reverseTranslation()
        self.turnOver = turnOver
        self.setting = 0
        self.offset = 0

    def setSetting(self, setting):
        self.setting = setting

    def setOffset(self, offset):
        self.offset = offset

    #create reverse permutation from the forward permutation
    def reverseTranslation(self):
        abc = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        index = 0
        for letter in self.permutation:
            self.reversePermutation[Translator.letterToIndex(letter)] = abc[index]
            index += 1

        print self.reversePermutation

    def forwardTranslation(self):
        pass