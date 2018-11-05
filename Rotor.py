from Translator import Translator

# this class represent a single rotor
class Rotor(Translator):
    SIZE = 26
    direction = "FORWARD"

    def __init__(self, name, permutation, turnOver):
        self.name = name
        self.permutation = permutation
        self.reversePermutation = [0] * self.SIZE
        self.reverseTranslation()  # create reverse translation from forward permutation
        self.turnOver = Translator.letterToIndex(turnOver)
        self.setting = 0
        self.offset = 0

    def setSetting(self, setting):
        self.setting = setting

    def setOffset(self, offset):
        self.offset = offset

    # create reverse permutation from the forward permutation
    def reverseTranslation(self):
        abc = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        index = 0
        for letter in self.permutation:
            self.reversePermutation[Translator.letterToIndex(letter)] = abc[index]
            index += 1

    # encrypt a given letter
    def translation(self, letter):
        shift = self.circularShifts(letter, self.offset - self.setting)
        if self.direction == 'REVERSE':
            convert = self.reversePermutation[Translator.letterToIndex(shift)]
        else:
            convert = self.permutation[Translator.letterToIndex(shift)]

        shift = self.circularShifts(convert, (self.setting - 1) - (self.offset - 1))
        return shift

    def step(self):
        if self.offset == 25:
            self.offset = 0
        self.offset += 1

    def isTurnover(self):
        if self.offset == self.turnOver:
            return True

        return False

    def changeDirection(self):
        if self.direction == 'FORWARD':
            self.direction = 'REVERSE'
        else:
            self.direction = 'FORWARD'
