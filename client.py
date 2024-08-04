import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # create a socket object, specified the socket family and socket type

# host = '192.168.56.1'
host = socket.gethostname()  # get local machine name
port = 444  # arbitrary port number

clientsocket.connect((host, port))  # connect to the server
message = clientsocket.recv(1024)  # receive data from the server

clientsocket.close() # close the connection
print(message.decode('ascii'))  # print the data received from the server