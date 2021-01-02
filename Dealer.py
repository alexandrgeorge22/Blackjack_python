class Dealer:
    hand = []

    def __init__(self):
        self.handtotal = 0

    def get_card(self, pack):
        self.hand.append(pack.get_card())
        self.handtotal += self.hand[len(self.hand) - 1].value

    def reset_hand(self):
        self.hand.clear()
        self.handtotal = 0
