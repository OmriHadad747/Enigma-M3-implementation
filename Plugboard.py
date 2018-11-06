import sys

from Translator import Translator

class Plugboard(Translator):

    def __init__(self, pbConfiguration = None):
        self.permutation = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        self.setConfiguration(pbConfiguration)

    def setConfiguration(self, pbConfiguration):
        if 0 < len(pbConfiguration) <= 10:
            for pair in pbConfiguration:
                firstLetter = pair[0]
                firstIndex = Translator.letterToIndex(firstLetter)
                secondLetter = pair[1]
                secondIndex = Translator.letterToIndex(secondLetter)
                self.permutation[firstIndex] = secondLetter
                self.permutation[secondIndex] = firstLetter
        elif len(pbConfiguration) > 10:
            print "Error, Only 10 Paris Of Plugboard is allow. Bay-Bay"
            sys.exit(0)

    def translation(self, letter):
        return self.permutation[Translator.letterToIndex(letter)]

