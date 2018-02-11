import socket

sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)


sniffer.bind(('0.0.0.0', 0))

sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

print "sniffer is Listening for incomming conncetion" 

print sniffer.recvfrom(65535)

