from Translator import Translator

class Plugboard(Translator):

    def __init__(self, pbConfiguration):
        self.permutation = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

        if len(pbConfiguration) > 0:
            for pair in pbConfiguration:
                firstLetter = pair[0]
                firstIndex = Translator.letterToIndex(firstLetter)
                secondLetter = pair[1]
                secondIndex = Translator.letterToIndex(secondLetter)
                self.permutation[firstIndex] = secondLetter
                self.permutation[secondIndex] = firstLetter


        print "plugboard permutation: "
        print self.permutation

    def forwardTranslation(self, letter):
        self.permutation[Translator.letterToIndex(letter)]

    def reverseTranslation(self):
        pass