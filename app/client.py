import socket
import pymongo
from pymongo import MongoClient
from pymongo import AsyncMongoClient
from pymongo.errors import ConnectionFailure
import logging

header = 64 
port = 65531
format = 'utf-8'
disconnect_message = "!DISCONNECT"
server = "192.168.1.3"
addr =(server , port)

#Cheking if server is availiable
client = MongoClient()
try:
    client.admin.command('ping')
except ConnectionFailure:
    print("Server not available")

client.maxPoolSize(3)

client.connect(addr)

dblist = client.list_database_names()
if "db" in dblist:
  print("The database exists.")

try:
    with client.watch([{"$match": {"operationType": "insert"}}]) as stream:
        for insert_change in stream:
            print(insert_change)
except pymongo.errors.PyMongoError:
    # The ChangeStream encountered an unrecoverable error or the
    # resume attempt failed to recreate the cursor.
    logging.error("...")


def send(msg):
    message = msg.encode(format)
    msg_length = len(message)
    #its the first message that we send and we need to ensure that this message is 64 bytes long (header size)
    send_length = str(msg_length).encode(format)
    send_length += b' ' * (header - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(format))
input()
send() 
input()
send(disconnect_message)