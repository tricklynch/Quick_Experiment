from socket import *
import sys

try:
    input = raw_input
except:
    input = input

ip = ""
if len(sys.argv) == 2:
    ip = sys.argv[1]
else:
    ip = input("Please input the target ip: ")

PORT = 80
MESSAGE = "Hello"

s = socket(AF_INET, SOCK_DGRAM)
s.sendto(MESSAGE, (ip, PORT))
