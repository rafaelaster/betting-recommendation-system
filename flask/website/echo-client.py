import socket

host = "127.0.0.1"
port = 65432

with socket.socket(socket.AF_INET , socket.SOCK_STREAM) as s:
    s.connect((host,port))

    # data is exchanged and connection is established
    s.sendall(b"Hellow , world")
    data = s.recv(1024)

print(f"Receieved {data}")