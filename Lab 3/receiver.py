import socket
import struct
import sys

# implementation based on https://stackoverflow.com/questions/603852/how-do-you-udp-multicast-in-python
GROUP = sys.argv[1]
PORT = int(sys.argv[2])
SCIPER = sys.argv[3]

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind((GROUP, PORT))

mreq = struct.pack("4sl", socket.inet_aton(GROUP), socket.INADDR_ANY)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

while True:
    print(sock.recv(4096))


