class Player:
    hand = []

    def __init__(self, name, surname, age, nationality, tokens):
        self.name = name
        self.surname = surname
        self.age = age
        self.nationality = nationality
        self.tokens = int(tokens)
        self.handtotal = 0
        self.bust = False
        self.bet = 0

    def get_card(self, pack):
        self.hand.append(pack.get_card())
        self.handtotal += self.hand[len(self.hand) - 1].value
        if self.handtotal > 21:
            self.bust = True

    def bet_tokens(self, tokensno):
        if self.tokens == 0:
            print("Out of tokens")
        elif self.tokens >= int(tokensno):
            self.bet = int(tokensno)
            self.tokens -= int(tokensno)
        else:
            print("Invalid bet, insufficient tokens. Available tokens = " + str(self.tokens))
            self.bet_tokens(input("Try again: "))

    def reset_hand(self):
        self.hand.clear()
        self.bet = 0
        self.handtotal = 0
        self.bust = False
