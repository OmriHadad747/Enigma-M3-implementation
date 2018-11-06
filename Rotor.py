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
        self.turnOver = Translator.letterToIndex(turnOver) + 1
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
        toEncrypt1 = self.circularShifts(letter, self.offset - self.setting)

        if self.direction == 'REVERSE':
            toEncrypt2 = self.reversePermutation[Translator.letterToIndex(toEncrypt1)]
        else:
            toEncrypt2 = self.permutation[Translator.letterToIndex(toEncrypt1)]

        encrypted = self.circularShifts(toEncrypt2, (self.setting - 1) - (self.offset-1))
        return encrypted

    def step(self):
        if self.offset == 26:
            self.offset = 1
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
