from socket import *

HOST = ''
PORT = 80

s = socket(AF_INET, SOCK_DGRAM)
s.bind((HOST, PORT))
data = s.recvfrom(1024)
print(data[0])
