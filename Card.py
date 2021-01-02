class Card:
    def __init__(self, type, sign, value):
        self.type = type
        self.value = value
        self.sign = sign

    def printCard(self):
        print(str(self.type) + " " + str(self.sign) + " " + str(self.value))
