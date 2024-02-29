import socket
import os

#Host to listen to

HOST = '192.168.1.203'

def main():
    if os.name == 'nt':
        socket_protocol = socket.IPPROTO_IP
    else:
        socket_protocol = socket.IPPROTO_ICMP
       #include ip header in the capture
    sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket_protocol)

    if os.name == 'nt':
        sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
    print(sniffer.recv(65565))

    # if we are on windows switch off promiscous mode

    if os.name == 'nt':
        sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)

main()