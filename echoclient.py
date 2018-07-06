import socket
UDP_IP_ADDRESS="127.0.0.1"
UDP_PORT_NUMBER=6789
message=("Hello")
bytestosend=str.encode(message)
clientsock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
clientsock.sendto(bytestosend,(UDP_IP_ADDRESS,UDP_PORT_NUMBER))
messagefromserver=clientsock.recvfrom(1024)
print(messagefromserver)
