from dog_detection import Vision
import socket
from dispenser import Control2
from history import History

vis = Vision()
hist = History()
HOST = "192.168.50.217" # IP address of your Raspberry PI
PORT = 65432          # Port to listen on (non-privileged ports are > 1023)

# while True:
#     dc = vis.check_dog() 
#     if dc is not None:
#         print(dc)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    cntl = Control2()

    try:
        while 1:
            #TODO VISION
            dc = vis.check_dog()
            hist.add_position(dc)

            #TODO AUDIO
            

            #TODO CHAT
            client, clientInfo = s.accept()
            print("server recv from: ", clientInfo)
            data = client.recv(1024)      # receive 1024 Bytes of message in binary format
            if data != b"":
                print(data)  
                orientation, traveled, obstacle = cntl.move(data)
                message= f"{orientation},{traveled},{obstacle}".encode('ascii')
                client.sendall(message) # Echo back to client
    except Exception as e:
        print('error: ', e)
        print("Closing socket")
        client.close()
        s.close()