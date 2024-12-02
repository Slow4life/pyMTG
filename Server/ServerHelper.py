# Send message to all connections
def sendToSockets(string, socketList):      
    for i in socketList:
        i.send(string.encode())

def sendToSocket(string, socketList):
    socketList.send(string.encode())