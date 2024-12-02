import time
import threading

from socket import *

# Initiate constants
SERVER_PORT = 6970
BUFFER_SIZE = 2048

#Lists
ipList = []
dealtHands = []

# Socket
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', SERVER_PORT))

# Creates a thread whenever a new connection is made
def listenForConnections():

    while(True):
    
        serverSocket.listen(1)

        connectionSocket, addr = serverSocket.accept()
        
        threadListenForMessages = threading.Thread(target = listenForMessages, args = (connectionSocket, addr, ))
        threadListenForMessages.start()
        
        ipList.append(connectionSocket)

# Handles connection loss, as well as incoming messages
def listenForMessages(socket, address):

    try:
    
        while(True):
        
            recvMsg = socket.recv(BUFFER_SIZE)
            recvMsg = recvMsg.decode()

            print(recvMsg)
            
    except:
        
        str = ''
        
        str = f'{address}'
        
        print(str + " has disconnected.")
        ipList.remove(socket)

threadListenForConnections = threading.Thread(target = listenForConnections)
threadListenForConnections.start()

# Admin commands
while(True):

    command = input("Command: ")
    
    if (command == "print"):
        
        print(ipList)
        
    elif (command == "print array"):
        
        for i in ipList:
        
            print(i)
        
    elif (command == "send"):
    
        msg = input("message: ")
        msg = msg.encode()
        
        for i in ipList:
            
            i.send(msg)
        
    elif (command == "threads"):
        
        for thread in threading.enumerate():
        
            print(thread.name)
        
    else:
    
        print("Command not recognized.")

