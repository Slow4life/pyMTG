def printHand(array, width):
    one = ""
    two = ""
    three = ""
    four = ""
    five = ""
    six = ""
    seven = ""
    eight = ""
    nine = ""
    print("Hand:")
    for card in array:
        if card.id == "la":
            one += "╔════════════╗"
        else:
            one += "╔═════════[" + f'{card.cost}' + "]╗"
        two += "║ " + card.name.ljust(width - 4, " ") + " ║"
        three += "╠════════════╣"
        four += "║" + card.art[0] + "║"
        five += "║" + card.art[1] + "║"
        six += "║" + card.art[2] + "║"
        seven += "╠════════════╣"
        eight += "║ " + card.description.ljust(width - 4, " ") + " ║"
        if card.id == "cr":
            nine += "╚═══════[" + f'{card.power}' + "/" + f'{card.toughness}' + "]╝"
        else:
            nine += "╚════════════╝"
    print(one)
    print(two)
    print(three)
    print(four)
    print(five)
    print(six)
    print(seven)
    print(eight)
    print(nine)

def printBoard(array, width):
    one = ""
    two = ""
    three = ""
    four = ""
    five = ""
    six = ""
    seven = ""
    for card in array:
        one += "╔════════════╗"
        two += "║" + card.art[0] + "║"
        three += "║" + card.art[1] + "║"
        four += "║" + card.art[2] + "║"
        five += "╠════════════╣"
        six += "║ " + card.description.ljust(width - 4, " ") + " ║"
        if card.id == "cr":
            seven += "╚═══════[" + f'{card.power}' + "/" + f'{card.toughness}' + "]╝"
        else:
            seven += "╚════════════╝"
    print(one)
    print(two)
    print(three)
    print(four)
    print(five)
    print(six)
    print(seven)