from abc import ABCMeta, abstractmethod

class Substitutor (ABCMeta):

    permutation = []

    @abstractmethod
    def forwardTranslation(self):
        pass

    @abstractmethod
    def reverseTranslation(self):
        pass

    def letterToIndex(self, letter):
        return letter - 'A'

    def indexToLetter(self, index):
        return index + 'A'

    def circularShifts(self, letter, index):
        if index < 0:
            index += 26
        return self.indexToLetter((self.letterToIndex(letter) + index) % 26)


