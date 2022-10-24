#playerNmbr är antalet spelare (2-10)
import time

def serverStartInput(answer, prompt):
    while True:
        inputAnswer = input(prompt).lower()
        if inputAnswer == answer:
            print("Done")
            global notStarted
            notStarted = False
            print(notStarted)
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
        serverSocket.listen(10)
        serverSocket.settimeout(0.5)
        
        #Startar en thread som stänger loopen när en viss input ges [WIP]
        starterThread.start()
        ls = LoopStopper(5)
        while notStarted:
            print("waiting")
            ls.run(range(10), lambda: acceptLoop(serverSocket))
            time.sleep(2)

            
        #Dbg
        print("Outside loop!")



#Inte min kod, tagen från Tony Flury, https://www.quora.com/In-Python-how-can-I-skip-an-iteration-in-a-for-loop-if-it-takes-longer-than-5-secs
from threading import Timer 
class LoopStopper: 
 
    def __init__(self, seconds): 
        self._loop_stop = False
        self._seconds = seconds
  
    def _stop_loop(self): 
        self._loop_stop = True 
    
    def run(self, generator_expression, task): 
        t = Timer(self._seconds, self._stop_loop) 
        t.start() 
        for _ in generator_expression: 
            task() 
            if self._loop_stop: 
                break 
        t.cancel()



def acceptLoop(serverSocket):
    try:
        clientSocket, address = serverSocket.accept()
        print(f'{address} connected to the game! Input "start" to end the connection phase')
        clientSocket.send(bytes("You have succesfully connected to the game!", "utf-8"))
        #Appenda till lista [WIP]
        return clientSocket, address
    except:
        pass



startServer()