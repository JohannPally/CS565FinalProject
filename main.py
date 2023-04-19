from dog_detection import Vision
import socket
from dispenser import Control2
from history import History
from sound import Sound

vis = Vision()
hist = History()
snd = Sound()
HOST = "192.168.50.217" # IP address of your Raspberry PI
PORT = 65432          # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    cntl = Control2()

    try:
        while 1:
            #VISION
            dc = vis.check_dog()
            hist.add_position(dc)

            #AUDIO
            samp = snd.get_sample()
            hist.add_sample(samp)

            #CHAT
            client, clientInfo = s.accept()
            print("server recv from: ", clientInfo)
            data = client.recv(1024)

            #STOP
            if data == b"stop":
                print("Closing socket")
                client.close()
                s.close()
                break

            if data != b"":
                print(data)  
                trts = cntl.act(data)
                if trts is not None:
                    message= f"Nova has gotten {trts} treats today!".encode('ascii')
                    client.sendall(message) # Echo back to client
    except Exception as e:
        print('error: ', e)
        print("Closing socket")
        client.close()
        s.close()