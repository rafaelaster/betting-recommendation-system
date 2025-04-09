import socket
import threading
import time

HEADER = 64 #64 bytes
PORT = 5000
#SERVER ="192.168.1.3"
#gets the ip address automatically
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
format = 'utf-8'
DISCONNECT_MESSAGE = "DISCONNECT!"
print(socket.gethostname())

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #af_inet =ivn4
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # <-- CRITICAL FIX



server.bind(ADDR)

#handling individual connections
def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    connected = True
    while connected:
       # we will not pass this line of coce until we receive a message from our client 
       msg_length = conn.recv(HEADER).decode(format)
       #we ensure that the message we received is valid
       if msg_length:
          msg_length = int(msg_length)
          msg = conn.recv(msg_length).decode(format)
          if msg == DISCONNECT_MESSAGE:
            connected = False
          print(f"[{addr}] {msg}")
          conn.send("Msg received".encode(format))

    conn.close()

#handling and distributing connections
def start():
    server.listen()
    print(f"[LISTENING ] Server is listening on {SERVER}")
    while True:
      conn , addr = server.accept()
      thread = threading.Thread(target= handle_client, args=(conn , addr))
      thread.start()
      print(f"[ACTIVE CONNECTIONS] {threading.active_count()-1}")

print("[STARTING] server is starting...")
start()