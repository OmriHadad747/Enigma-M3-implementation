from Translator import Translator

class Reflector(Translator):

    def __init__(self, permutation):
        self.permutation = permutation

    def translation(self, letter):
        return self.permutation[Translator.letterToIndex(letter)]
