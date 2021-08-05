import socket
import select
import sys

# A socket object is created with an address family for IPv4 and TCP socket type.
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

if len(sys.argv) != 3:
	print ("How to make it work: script, IP address, PORT number")
	exit()

# The first argument from the prompt is saved in IP_ADDRESS as a IP address.
IP_ADDRESS = str(sys.argv[1])

# The second argument from the prompt is saved in PORT as a port number.
PORT = int(sys.argv[2])
server.connect((IP_ADDRESS, PORT))

while True:
    #Keeps the list of messages that will be send to the server
    sockets_list = [sys.stdin, server]

    read_sockets,write_socket, error_socket = select.select(sockets_list,[],[])
    for socks in read_sockets:
	if socks == server:
            message = socks.recv(2048)
            # The message is printed and decoded()
	    print (message.decode())
	else:
            message = sys.stdin.readline()
            # The message is encoded.
       	    server.send(bytes(message,'utf-8'))
	    sys.stdout.write("<Me>")
	    sys.stdout.write(message)
	    sys.stdout.flush()
            
server.close()
