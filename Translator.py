
class Translator():

    def forwardTranslation(self):
        pass

    def reverseTranslation(self):
        pass

    @staticmethod
    def letterToIndex(letter):
        letter = map(ord, letter)
        constLetter = map(ord, 'A')
        return letter[0] - constLetter[0]

    @staticmethod
    def indexToLetter(index):
        return index + 'A'

    def circularShifts(self, letter, index):
        if index < 0:
            index += 26
        return self.indexToLetter((self.letterToIndex(letter) + index) % 26)





