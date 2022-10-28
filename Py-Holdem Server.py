#playerNmbr är antalet spelare (2-10)
import time
socketBox = []
addressBox = []


def serverStartInput(answer, prompt):
    while True:
        inputAnswer = input(prompt).lower()
        if inputAnswer == answer:
            print("Done!")
            global notStarted
            notStarted = False
            break



def startServer():
    global notStarted
    notStarted = True
    import socket
    import threading
    PORT = 42069
    starterThread = threading.Thread(target=serverStartInput, args=["start", 'Input "start" to end the connection phase\n'])

    #sätter variabeln serverSocket som en socket med TCP protokoll och IPV4-anslutning
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serverSocket:
        serverSocket.bind((socket.gethostname(), PORT))
        print(socket.gethostname(), PORT)
        serverSocket.listen(10)
        serverSocket.settimeout(0.5)
        
        #Startar en thread som stänger loopen när en viss input ges [WIP]
        starterThread.start()
        while notStarted:
            acceptLoop(serverSocket)
        print("Next phase!")

        '''game = True
        while game:
            sendToAll(socketBox, f"Game has started with {len(addressBox)} players!")'''

            



#Tar emot requests, sitter på timeout
def acceptLoop(serverSocket):
    try:
        clientSocket, address = serverSocket.accept()
        socketBox.append(clientSocket)
        addressBox.append(address)
        print(f'{address} connected to the game! Input "start" to end the connection phase')
        playerID = "player " + str(socketBox.index(clientSocket)+1)
        clientSocket.send(bytes(f"You have succesfully connected to the game as {playerID}!", "utf-8"))
    except:
        pass



#Skickar ett meddelande till alla anslutna enheter
def sendToAll(socketBox, message):
    for i in range(len(socketBox)):
        currentClientSocket = socketBox[i]
        currentClientSocket.send(bytes(message, "utf-8"))




startServer()