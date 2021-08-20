import socket
import select
import sys
from _thread import *


# A socket object is created with an address family for IPv4 and TCP socket type. 
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Checks if the number of arguments is given is correct.
if len(sys.argv) != 3:
	print ("Correct usage: script, IP address, port number")
	exit()
        
# The first argument from the prompt is saved in IP_ADDRESS as a IP address.
IP_ADDRESS = str(sys.argv[1])

# The second argument from the prompt is saved in PORT as a port number.
PORT = int(sys.argv[2])

server.bind((IP_ADDRESS, PORT))
server.listen(100)

# List were all the future clients will be saved.
list_of_clients = []

def client_thread(conn, addr):
    # Sends a welcome message to the just connected clientt whose user object is conn.
    conn.send(bytes("Welcome to the chatroom!", 'utf-8'))
    while True:
        try:
            message = conn.recv(2048).decode()
            if(message):
                print ("<" + str(addr[0]) + "> " + message)
       	        # Calls broadcast function to send client message to the rest of clients.
                message_to_send = "<" + str(addr[0]) + "> " + message
                spread_the_voice(message_to_send, conn)                
            else:
                remove(conn)
        except:
            continue

def spread_the_voice(message, connection):
    for client in list_of_clients:
        if client!=connection:
            try:
                # Before sending the message, it is encoded().
                client.send(message.encode())
            except:
                client.close()
                # The client is remove if the link with it is broken.
                remove(client)

def remove(connection):
    if connection in list_of_clients:
        # A client connection is remove.
        list_of_clients.remove(connection)

while True:
        
    conn, addr = server.accept()
    list_of_clients.append(conn)

    # Prints the address of the Client that just connected
    print (addr[0] + " connected")

    # For each user that connects a thread is created.
    start_new_thread(client_thread,(conn,addr))	

conn.close()
server.close()

