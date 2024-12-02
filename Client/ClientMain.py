from socket import *
import os
import threading

import ClientHand as Hand
import ClientBoard as Board
#import ClientCreatures as Creature
from ClientCreatures import *

# Initiate Port
serverPort = 6969
clientSocket = socket(AF_INET, SOCK_STREAM)

def validateIP(address):

	fields = address.split(".")
    
	if (len(fields) != 4):
		print("IP format: \"xxx.xxx.xxx.xxx\"")
		return False
        
	for field in fields:
    
		try:
			int(field)
            
		except ValueError:
			print("IP has to consist of integers only.")
			return False
            
		if (not 0 <= int(field) <= 255):
			print("IP cell range: 0..255.")
			return False
            
	return True
    
def validateConnection():

    validServerName = False
    connected = False

    while(validServerName == False or connected == False):

        serverName = input("Server address: ")
        validServerName = validateIP(serverName)

        if (validServerName):
            try:
                print("Connecting...")
                clientSocket.connect((serverName,serverPort))
                connected = True
            except BaseException as e1:
                print("Server could not reached. Make sure to type server address correctly.")
                print(e1)

    if (connected == True):
        print("Connection successful.")
        
    else:
        print("Connection failed.")
        
validateConnection()

def commands(currentMana, maxMana):
    print("Library size: " + f'{len(hand.deck.deck)}' + ". Current mana: " + f'{currentMana}' + "/" + f'{maxMana}' + ".")
    print("Actions: 'play', 'pass'.")

def cmdReset(string):
    os.system("cls")
    #print(str(hand.hand[0]))
    board.printBoard()
    hand.printHand()
    if len(string) == 0:
        pass
    else:
        print(string)

hand = Hand.Hand()

board = Board.Board()
        
def listenForMessages():
    
    while True:
        recvMsg = clientSocket.recv(2048)
        recvMsg = recvMsg.decode()
        if recvMsg == "start":
            hand.mulligan()
            os.system("cls")
            hand.printHand()
            ready = False
            while not ready:
                prompt = input("'mulligan' or 'ready': ")
                if prompt == "mulligan":
                    os.system("cls")
                    hand.mulligan()
                    hand.printHand()
                elif prompt == "ready":
                    ready = True
                    hand.keepHand()
                    clientSocket.send(prompt.encode())
                    print("Waiting for other players.")
                else:
                    print("You're a dumbass. Try again.")
        elif recvMsg == "first" or recvMsg == "go":
            # Draw only if you're not first to act and hand size is < maxHandSize.
            if recvMsg == "go" and hand.getHandSize() < hand.maxHandSize:
                hand.draw()
                cmdReset("You drew " + f'{hand.hand[hand.getHandSize() - 1].name}' + ".")
            else:
                cmdReset("No card draw for you... bitch.")
            playedLand = False
            currentMana = hand.mana
            while True:
                commands(currentMana, hand.mana)
                command = input("Action: ")
                if command == "play":
                    cardNum = input("Card (1-" + f'{len(hand.hand)}' + "): ")
                    try:
                        tempHandSize = hand.getHandSize()
                        if int(cardNum) and int(cardNum) > 0 and int(cardNum) <= len(hand.hand):
                            # If creature is played
                            if hand.hand[int(cardNum)-1].id == "cr":
                                if hand.hand[int(cardNum)-1].cost <= currentMana:
                                    #card = hand.hand[int(cardNum)-1]
                                    cardName = hand.hand[int(cardNum)-1].name
                                    temp = hand.hand.pop(int(cardNum)-1)
                                    currentMana -= temp.cost
                                    board.ownBoard.append(temp)
                                    cmdReset("You've played " + cardName + ".")
                                    clientSocket.send(("cr-" + cardName).encode())
                                else:
                                    cmdReset("Not enough mana.")
                            # If land is played
                            elif hand.hand[int(cardNum)-1].id == "la":
                                if not playedLand:
                                    cardName = hand.hand[int(cardNum)-1].name
                                    hand.increaseMana()
                                    currentMana += 1
                                    hand.hand.pop(int(cardNum)-1)
                                    hand.printHand()
                                    playedLand = True
                                    cmdReset("You've played " + cardName + ".")
                                else:
                                    cmdReset("You've already played a land this turn.")
                            elif hand.hand[int(cardNum)-1].id == "ki":
                                if len(board.enemyBoard) > 0:
                                    if hand.hand[int(cardNum)-1].cost <= currentMana:
                                        target = input("Target (1-" + f'{len(board.enemyBoard)}' + "): ")
                                        temp = board.enemyBoard.pop(int(target)-1)
                                        currentMana -= hand.hand[int(cardNum)-1].cost
                                        hand.hand.pop(int(cardNum)-1)
                                        clientSocket.send(("ki-" + target).encode())
                                        cmdReset("You destroyed " + temp.name + ".")
                                    else:
                                        cmdReset("Not enough mana.")
                                else:
                                    cmdReset("Opponent has no creatures on board.")
                        elif int(cardNum) and int(cardNum) < 1:
                            cmdReset("Less than one? Now, don't be a dumbass.")
                        elif int(cardNum) > tempHandSize:
                            cmdReset("Use your fingers to count if needed. Now, don't be a dumbass.")
                    except BaseException as e1:
                        cmdReset("Something went wrong. Try again.")
                        #print(e1)
                elif command == "pass":
                    cmdReset("You've passed your turn.")
                    clientSocket.send(command.encode())
                    break
                else:
                    cmdReset("You're a dumbass. Try again.")

        elif recvMsg.startswith("cr-"):
            temp = recvMsg[3:]
            creature = globals()[temp]
            brackets = creature()
            board.enemyBoard.append(brackets) # Unsafe, apparently TEMPORARY
            cmdReset("Opponent is doing their turn.\nOpponent has played " + temp + ".")

        elif recvMsg.startswith("ki-"):
            temp = int(recvMsg[3:])
            print(temp)
            if len(board.ownBoard) > 0:
                target = board.ownBoard[temp-1].name
                board.ownBoard.pop(temp-1)
                cmdReset("Opponent is doing their turn.\nOpponent has destroyed your " + target + ".")

        elif recvMsg == "upnext":
            cmdReset("Opponent is doing their turn.")

threadListenForMessages = threading.Thread(target = listenForMessages)
threadListenForMessages.start()