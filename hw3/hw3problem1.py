# PUT YOUR NAME HERE
# PUT YOUR SBU ID NUMBER HERE
# PUT YOUR NETID (BLACKBOARD USERNAME) HERE
#
# IAE 101 (Fall 2021)
# HW 3, Problem 1

# DON'T CHANGE OR REMOVE THIS IMPORT
from random import shuffle

# DON'T CHANGE OR REMOVE THESE LISTS
# The first is a list of all possible card ranks: 2-10, Jack, King, Queen, Ace
# The second is a list of all posible card suits: Hearts, Diamonds, Clubs, Spades
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
suits = ["H", "D", "C", "S"]

# This class represents an individual playing card
class Card():
    def __init__(self, suit="", rank=""):
        # pass # REMOVE THIS AND REPLACE WITH YOUR CODE
        self.suit = str(suit)
        self.rank = str(rank)

    # DON'T CHANGE OR REMOVE THIS
    # This function creates a string out of a Card for easy printing.
    def __str__(self):
        return "[" + self.suit + ", " + self.rank + "]"

# This class represents a deck of playing cards
class Deck():
    def __init__(self, cards=[]):
        # pass # REMOVE THIS AND REPLACE WITH YOUR CODE
        self.cards = []
        for i in range(13):
            for j in range(4):
                self.cards.append(Card(suits[j], ranks[i]))        
    # DON'T CHANGE OR REMOVE THIS
    # This function will shuffle the deck, randomizing the order of the cards
    # inside the deck.
    # It takes an integer argument, which determine how many times the deck is
    # shuffled. 

    def shuffle_deck(self, n=5):
        for i in range(n):
            shuffle(self.cards)

    # This function will deal a card from the deck. The card should be removed
    # from the deck and added to the player's hand.
    def deal_card(self, player):
        # pass # REMOVE THIS AND REPLACE WITH YOUR CODE
        self.player = player
        self.player.hand.append(self.cards[0])
        del self.cards[0]

    # DON"T CHANGE OR REMOVE THIS
    # This function constructs a string out of a Deck for easy printing.
    def __str__(self):
        res = "[" + str(self.cards[0])
        for i in range(1, len(self.cards)):
            res += ", " + str(self.cards[i])
        res += "]"
        return res

# This class represents a player in a game of Blackjack
class Player():
    def __init__(self, name="", hand=[], status=True):
        # pass # REMOVE THIS AND REPLACE WITH YOUR CODE
        self.name = str(name)
        self.hand = []
        self.status = True

    def value(self):
        # pass # REMOVE THIS AND REPLACE WITH YOUR CODE
        sumhand = 0
        for i in range(len(self.hand)):
            if self.hand[i].rank in ["2", "3", "4", "5", "6", "7", "8", "9", "10"]:
                sumhand += int(self.hand[i].rank)
            elif self.hand[i].rank in ["J", "Q", "K"]:
                sumhand += 10
            elif self.hand[i].rank == "A":
                if sumhand + 11 > 21:
                    sumhand += 1
                else:
                    sumhand += 11
        if sumhand > 21:
            self.status = False
        return sumhand

    def choose_play(self):
        # pass # REMOVE THIS AND REPLACE WITH YOUR CODE
        if self.value() > 17:
            return "Stay"
        else:
            return "Hit"

    # DON'T CHANGE OR REMOVE THIS
    # This function creates a string representing a player for easy printing.
    def __str__(self):
        res = "Player: " + self.name + "\n"
        res += "\tHand: " + str(self.hand[0])
        for i in range(1, len(self.hand)):
            res += ", " + str(self.hand[i])
        res += "\n"
        res += "\tValue: " + str(self.value())
        return res

# This class represents a game of Blackjack
class Blackjack():
    def __init__(self, players, deck=Deck()):
        # pass # REMOVE THIS AND REPLACE WITH YOUR CODE
        self.players = []
        self.deck = Deck()
        self.deck.shuffle_deck(10)
        for i in range(len(players)):
            p = Player(players[i].name)
            self.deck.deal_card(p)
            self.deck.deal_card(p)
            self.players.append(p)

    def play_game(self):
        # pass # REMOVE THIS AND REPLACE WITH YOUR CODE
        while True:
            for i in range(len(self.players)):
                if self.players[i].status is True:
                    if self.players[i].choose_play() == "Hit":
                        self.deck.deal_card(self.players[i])
                        if self.players[i].value() > 21:
                            print("The player " + self.players[i].name + " has busted!\r\n")
                            self.players[i].status = False
                    else:
                        self.players[i].status = False
            cntP = 0
            for i in range(len(self.players)):
                if self.players[i].status is False:
                    cntP += 1
                else:
                    break
            if cntP == len(self.players):
                break
        maxpoint = 0
        winners = []
        for i in range(len(self.players)):
            curPoint = self.players[i].value()
            if curPoint <= 21:
                if curPoint > maxpoint:
                    maxpoint = curPoint
                    winners = []
                    winners.append(self.players[i].name)
                elif curPoint == maxpoint:
                    winners.append(self.players[i].name)
        if len(winners) == 0:
            print("No winner!\r\n")
        elif len(winners) == 1:
            print("Winner is " + winners[0])
        else:
            res = ""
            for i in range(len(winners)):
                res += winners[i]
                if i != len(winners) - 1:
                    res += ", "
            print("There is a tie, winners are " + res)

    # DON'T CHANGE OR REMOVE THIS
    # This function creates a string representing the state of a Blackjack game
    # for easy printing.
    def __str__(self):
        res = "Current Deck:\n\t" + str(self.deck)
        res = "\n"
        for p in self.players:
            res += str(p)
            res += "\n"
        return res

# DO NOT DELETE THE FOLLOWING LINES OF CODE! YOU MAY
# CHANGE THE FUNCTION CALLS TO TEST YOUR WORK WITH
# DIFFERENT INPUT VALUES.
if __name__ == "__main__":
    # Uncomment each section of test code as you finish implementing each class
    # for this problem. Uncomment means remove the '#' at the front of the line
    # of code.

    # Test Code for your Card class
    c1 = Card("H", "10")
    c2 = Card("C", "A")
    c3 = Card("D", "7")

    print(c1)
    print(c2)
    print(c3)

    print()

    # Test Code for your Deck class
    d1 = Deck()
    d1.shuffle_deck(10)
    print(d1)

    print()

    # Test Code for your Player class
    p1 = Player("Alice")
    p2 = Player("Bob")
    d1.deal_card(p1)
    d1.deal_card(p2)
    print(p1.value())
    print(p2.value())
    d1.deal_card(p1)
    d1.deal_card(p2)
    print(p1.value())
    print(p2.value())
    d1.deal_card(p1)
    d1.deal_card(p2)
    print(p1.value())
    print(p2.value())
    print(p1)
    print(p2)
    print(p1.choose_play())
    print(p2.choose_play())

    print()

    # Test Code for your Blackjack class
    terrible_people = [Player("Summer"), Player("Rick"), Player("Morty"), Player("Jerry")]
    game = Blackjack(terrible_people)
    print(game)
    game.play_game()
    print(game)
