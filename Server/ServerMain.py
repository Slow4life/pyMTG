#NOTES::::::::::::::::
#Shift all list indices to right: z.insert(0,z.pop())

import threading

from socket import *

import ServerHelper as Helper

# Initiate constants
SERVER_PORT = 6969
BUFFER_SIZE = 2048

#Lists
ipList = []
connectionList = []
dealtHands = []

# Socket
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', SERVER_PORT))

print("Server is running.")

# Creates a thread whenever a new connection is made
def listenForConnections():

    while(True):
    
        serverSocket.listen(1)

        connectionSocket, address = serverSocket.accept()
        
        threadListenForMessages = threading.Thread(target = listenForMessages, args = (connectionSocket, address))
        threadListenForMessages.start()

        print(f'{address}' + " has connected.")

        if len(connectionList) > 0:
            Helper.sendToSockets("Opponent has been found.", connectionList)
        
        connectionList.append(connectionSocket)
        ipList.append(address)

        print("Connection count: " + f'{len(connectionList)}')

        if len(connectionList) >= 2:
            Helper.sendToSockets("start", connectionList)
            break
    return

readyCounter = 0

# Handles connection loss, as well as incoming messages
def listenForMessages(socket, address):

    global readyCounter
    readyCounter = 0

    try:
        while(True):
            recvMsg = socket.recv(BUFFER_SIZE)
            recvMsg = recvMsg.decode()
            
            if recvMsg == "ready":
                readyCounter += 1
                print("Players ready: " + f'{readyCounter}')

            if readyCounter == 2:
                readyCounter = 0
                Helper.sendToSocket("first", connectionList[0])
                Helper.sendToSocket("upnext", connectionList[1])
                print("Match has begun.")

            if address == ipList[0]:
                if recvMsg == "pass":
                    print("'pass' received from " + f'{address}')
                    Helper.sendToSocket("go", connectionList[1])
                    Helper.sendToSocket("upnext", connectionList[0])
                elif recvMsg.startswith("cr-"):
                    Helper.sendToSocket(recvMsg, connectionList[1])
                    print(str(address) + " played " + recvMsg)
                elif recvMsg.startswith("ki-"):
                    Helper.sendToSocket(recvMsg, connectionList[1])
                    print(str(address) + " played " + recvMsg)


            if address == ipList[1]:
                if recvMsg == "pass":
                    print("'pass' received from " + f'{address}')
                    Helper.sendToSocket("go", connectionList[0])
                    Helper.sendToSocket("upnext", connectionList[1])
                elif recvMsg.startswith("cr-"):
                    Helper.sendToSocket(recvMsg, connectionList[0])
                    print(str(address) + " played " + recvMsg)
                elif recvMsg.startswith("ki-"):
                    Helper.sendToSocket(recvMsg, connectionList[0])
                    print(str(address) + " played " + recvMsg)

            
    except BaseException as e1:
        
        print(f'{address}' + " has disconnected.")
        print(e1)
        ipList.remove(address)
        connectionList.remove(socket)
        print("Connection count: " + f'{len(connectionList)}')
        Helper.sendToSockets("Opponent has lost connection. You win.", connectionList)

threadListenForConnections = threading.Thread(target = listenForConnections)
threadListenForConnections.start()

# Server commands
while(True):

    command = input("")
    
    if (command == "print"):
        print(ipList)

    elif (command == "print array"):
        for i in ipList:
            print(i)

    elif (command == "send"):
        msg = input("message: ")
        msg = msg.encode()
        for i in connectionList:
            i.send(msg)
        
    elif (command == "threads"):
        
        for thread in threading.enumerate():
            print(thread.name)
        
    else:
        print("Command not recognized.")

