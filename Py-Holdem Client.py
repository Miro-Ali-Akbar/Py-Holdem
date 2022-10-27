def startClient():
    import socket
    PORT = 42069
    ADDR = (socket.gethostname(), PORT)


    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as clientSocket:
        clientSocket.connect(ADDR)
        print(ADDR)

        msg = clientSocket.recv(256)
        print(msg.decode("utf-8"))

startClient()