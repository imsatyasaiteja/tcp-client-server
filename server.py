import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # create a socket object, specified the socket family and socket type

# host = '192.168.56.1'
host = socket.gethostbyname()   # get local machine name
port = 444  # arbitrary port number

serversocket.bind((host, port)) # bind host and port together
serversocket.listen(3)  # starting a TCP listener which can listen to a maximum of 3 clients

while True:
    clientsocket, address = serversocket.accept()  # establish a connection
    print("Got a connection from %s" % str(address))
    clientsocket.send("Thank you for connecting".encode('ascii'))
    clientsocket.close()