class Skeleton:
    def __init__(self):
        self.id = "cr"
        self.name = "Skeleton"
        self.cost = 1
        self.power = 1
        self.toughness = 1
        self.haste = False
        self.description = ""
        self.art = ["   | ☻      ",
                    "   +-¥{}    ",
                    "    (|      "]

class Grizzly:
    def __init__(self):
        self.id = "cr"
        self.name = "Grizzly"
        self.cost = 2
        self.power = 2
        self.toughness = 2
        self.haste = False
        self.description = "Speed-AIDS"
        self.art = ["   ʕ•ᴥ•ʔ    ",
                    "  C( . )Ↄ   ",
                    "    U U     "]

class Ogre:
    def __init__(self):
        self.id = "cr"
        self.name = "Ogre"
        self.cost = 3
        self.power = 4
        self.toughness = 2
        self.haste = False
        self.description = "Overweight"
        self.art = [" { <O> <ø> }",
                    "  \  /_\  / ",
                    "  / v---v \\ "]