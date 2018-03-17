import socket, sys, struct

PORT = 8020
HOST = "localhost"
def askStatus():
    sock = socket.create_connection((HOST, PORT))
    try:        
        size = struct.unpack('!I', sock.recv(4))[0]
        data = sock.recv(size)       

        status = "Currently playing: " + data.decode('utf-8')
        print(status)
    finally:
        sock.close()


askStatus()
