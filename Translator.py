
# this class charge on letter to index and index to letter operation included circular shifts
class Translator:

    def __init__(self):
        pass

    def translation(self):
        pass

    def reverseTranslation(self):
        pass

    @staticmethod
    def letterToIndex(letter):
        num = ord(letter)
        return num - ord('A')

    @staticmethod
    def indexToLetter(index):
        return chr(index + ord('A'))

    def circularShifts(self, letter, index):
        if index < 0:
            index += 26

        return self.indexToLetter((self.letterToIndex(letter) + index) % 26)
