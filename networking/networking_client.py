import socket

s = socket.socket()  # create a socket object
HOST = 'localhost'
PORT = 5000

s.connect((HOST, PORT))
print(s.recv(1024))
s.close()
