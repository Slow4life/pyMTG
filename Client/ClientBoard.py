import ClientHelper as Helper

class Board:

    def __init__(self):
        self.enemyBoard = []
        self.ownBoard = []

    def printBoard(self):
        print("Enemy board:")
        if not len(self.enemyBoard):
            print("╔═")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("╚═")
        else:
            Helper.printBoard(self.enemyBoard, 14)
        print("Own board:")
        if not len(self.ownBoard):
            print("╔═")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("╚═")
        else:
            Helper.printBoard(self.ownBoard, 14)

