import ClientDeck as Deck
import ClientHelper as Helper

class Hand():

    def __init__(self):

        self.deck = Deck.Deck()
        self.hand = []
        self.mana = 0
        self.maxHandSize = 8

    def getDeck(self):
        return self.deck.deck

    def getHand(self):
        return self.hand

    def getHandSize(self):
        return len(self.hand)

    def getMana(self):
        return self.mana

    def increaseMana(self):
        self.mana += 1

    def mulligan(self):
        self.deck.shuffleDeck()
        self.hand = []
        for i in range(1, 8):
            self.hand.append(self.deck.deck[i-1])

    def keepHand(self):
        for i in range(1, 8):
            self.deck.deck.pop(i-1)

    def draw(self):
        self.hand.append(self.deck.deck.pop(0))

    def printHand(self):
        Helper.printHand(self.hand, 14)