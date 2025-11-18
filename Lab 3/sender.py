import socket
import struct
import sys

GROUP = sys.argv[1]
PORT = int(sys.argv[2])
SCIPER = sys.argv[3]

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

while True:
    msg = input("Enter the message to send: ")
    msg = SCIPER.encode() + msg.encode()
    sock.sendto(msg, (GROUP, PORT))




