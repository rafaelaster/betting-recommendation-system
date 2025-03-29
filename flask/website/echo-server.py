import socket

#Set up a listeign socket

host = "127.0.0.1"
#The port it listes to

port = 65432

with socket.socket(socket.AF_INET , socket.SOCK_STREAM) as s:
    s.bind((host,port))
    s.listen()
    conn , addr = s.accept()

# Data is exchanged

    with conn:
        print(f"Connected by{addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)