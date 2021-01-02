import Package as Package
import Player as Player
import Dealer as Dealer

if __name__ == '__main__':
    pack = Package.Package()
    pack.create_pack()
    pack.shuffle()
    dealer = Dealer.Dealer()

    f = open("ListaParticipanti.txt", "r")
    data = f.readlines()

    players = []
    for line in data:
        words = line.split()
        players.append(Player.Player(words[0], words[1], words[2], words[3], words[4]))

    print("List of players:")
    for player in players:
        print(str(player.name) + " " + str(player.surname) + " " + str(player.age) + " years old from " + str(
            player.nationality) + " with " + str(player.tokens) + " tokens")

    playersdata = []
    game = True
    round = 0
    while game:
        round += 1

        print("\nRound " + str(round) + "\n")
        if len(pack.pack) is 0:
            pack.create_pack()
            pack.shuffle()
        print("Players bet")
        for player in players:
            player.bet_tokens(input("Bet for player " + str(player.name) + ": "))
            player.get_card(pack)
            player.get_card(pack)
            print("Initial cards in hand for " + str(player.name) + " : " + str(player.handtotal))

        dealer.get_card(pack)
        print("\nDealer's initial card: " + str(dealer.handtotal) + "\n")

        for player in players:
            if not player.bust:
                print(str(player.name) + "'s turn")
                print("Total of cards in hand = " + str(player.handtotal))
                do = True
                while do:
                    if (player.handtotal == 21):
                        break
                    if player.bust:
                        print(str(player.name) + " bust")
                        break
                    choice = input("hit or stand? ")
                    if choice.__eq__("hit"):
                        player.get_card(pack)
                        print("Total of cards in hand = " + str(player.handtotal))
                    else:
                        do = False

        print("Dealer's turn")
        while dealer.handtotal < 17:
            dealer.get_card(pack)
            print("Total of cards for dealer: " + str(dealer.handtotal))

        if dealer.handtotal > 21:
            print("Dealer is bust, all the players that is not bust wins")
            for player in players:
                if not player.bust:
                    player.tokens += player.bet * 2

        if dealer.handtotal <= 21:
            for player in players:
                if not player.bust:
                    if player.handtotal > dealer.handtotal:
                        player.tokens += player.bet * 2
                        print(str(player.name) + " wins " + str(player.bet) + " tokens")
                    if player.handtotal == dealer.handtotal:
                        player.tokens += player.bet
                        print(str("Draw for " + player.name))

        actual_players = []
        for player in players:
            print(str(player.name) + "'s availeble tokens = " + str(player.tokens))
            player.reset_hand()
            if player.tokens == 0:
                print(str(player.name) + " is out of game")
                playersdata.append(player)
                continue
            cont = input("Continue the game? ")
            if cont.__eq__("yes"):
                actual_players.append(player)
            else:
                playersdata.append(player)

        players.clear()
        players = actual_players
        dealer.reset_hand()

        if not players:
            print("\nFinal of the game\n")
            for player in playersdata:
                print(str(player.name) + " " + str(player.surname) + " finish the game with " + str(
                    player.tokens) + " tokens")
            game = False
