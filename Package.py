from Card import Card
import random


class Package:
    # pack = set type

    def __init__(self):
        self.pack = []

    def create_pack(self):
        for i in range(2, 11):
            self.pack.append(Card("clubs", i, i))
            self.pack.append(Card("diamonds", i, i))
            self.pack.append(Card("hearts", i, i))
            self.pack.append(Card("spades", i, i))
        types = ["clubs", "diamonds", "hearts", "spades"]
        for type in types:
            self.pack.append(Card(type, "ace", 11))
            self.pack.append(Card(type, "king", 10))
            self.pack.append(Card(type, "queen", 10))
            self.pack.append(Card(type, "jack", 10))

    def shuffle(self):
        return random.shuffle(self.pack)

    def get_card(self):
        if len(self.pack) == 0:
            self.create_pack()
            self.shuffle()
        return self.pack.pop()
