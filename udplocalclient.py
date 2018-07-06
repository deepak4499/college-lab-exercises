import socket
UDP_IP_ADDRESS = "127.0.0.1"
UDP_PORT_NO = 6159
message=("welcome server")
bytestosend=str.encode(message)
clientsock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
clientsock.sendto(bytestosend,(UDP_IP_ADDRESS,UDP_PORT_NO))
