from Translator import Translator

class Plugboard(Translator):

    def __init__(self, pbConfiguration):
        self.permutation = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        self.setConfiguration(pbConfiguration)

    def setConfiguration(self, pbConfiguration):
        if len(pbConfiguration) > 0:
            for pair in pbConfiguration:
                firstLetter = pair[0]
                firstIndex = Translator.letterToIndex(firstLetter)
                secondLetter = pair[1]
                secondIndex = Translator.letterToIndex(secondLetter)
                self.permutation[firstIndex] = secondLetter
                self.permutation[secondIndex] = firstLetter

    def translation(self, letter):
        return self.permutation[Translator.letterToIndex(letter)]

