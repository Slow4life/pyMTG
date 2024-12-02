import random
import inspect
import ClientCreatures as Creature
import ClientSpells as Spell
import ClientLands as Land

class Deck:

    def __init__(self):

        self.deck = []
        self.cardList = []

        for name, obj in inspect.getmembers(Creature):
            if inspect.isclass(obj):
                self.cardList.append(name)

        for i in range(1, 25):
            self.deck.append(Land.Mountain())

        for i in range(1, 9):
            self.deck.append(Spell.Kill())

        for i in range(1, 11):
            self.deck.append(Creature.Skeleton())

        for i in range(1, 10):
            self.deck.append(Creature.Grizzly())

        for i in range(1, 10):
            self.deck.append(Creature.Ogre())

    def shuffleDeck(self):
        random.shuffle(self.deck)

    def printCardClasses(self):
        i = 0
        for card in self.cardList:
            print(self.cardList[i])
            i += 1
