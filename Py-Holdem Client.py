def startClient():
    import socket
    PORT = 34269

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as clientSocket:
        clientSocket.connect((socket.gethostname(), PORT))

        while True:
            msg = clientSocket.recv(256)
            print(msg.decode("utf-8"))