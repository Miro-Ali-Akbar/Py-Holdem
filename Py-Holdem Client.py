import time


def startClient():
    import socket
    PORT = 42069
    ADDR = (socket.gethostname(), PORT)


    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as clientSocket:
        clientSocket.connect(ADDR)
        print(ADDR)

        msg = clientSocket.recv(256)
        print(msg.decode("utf-8"))



#WIP from now on... Enter at your own risk
def interpretSignal(functionCall, clientSocket):
    functionCall(clientSocket)



def printMessage(clientSocket):
    msg = clientSocket.recv(256)
    print(msg.decode("utf-8"))



def demandInput(clientSocket):
    answer = input("Do you wish to bet, raise, call or fold?")
    lowerAnswer = answer.lower()
    if answer in ["bet", "raise", "call", "fold"]:
        clientSocket.send(bytes(lowerAnswer, "utf-8"))





startClient()