import argparse
from socket import *

"""USAGE python targetscaner.py -a 192.168.0.1 -p 21,80"""


def printbanner(connsocket,tgtPort):
	try:
		if (tgtPort == 80):
			connsocket.send("GET HTTP/1.1 \r \n")
		else:
			connsocket.send("\r \n")
		 #Rescive a data
		result = connsocket.recv(4096)
		
		print "++>> BANNER :" + str(result)  
	except:
		print "++>> BANNER not available"

def conscanTcp(tgthost,tgtPort):
	try:
		# creaating a socket
		connsocket = socket(AF_INET, SOCK_STREAM)
		# connect to target
		connsocket.connect((tgthost,tgtPort))
		print "++>> %d Tcp OPEN " % tgtPort
		printbanner(connsocket,tgtPort)
	except:
		print "++>> %d TCP CLOSED " % tgtPort
	finally:
		connsocket.close()

def conscanUdp(tgthost,tgtPort):
	try:
		# creaating a socket
		connsocket = socket(AF_INET, SOCK_DGRAM)
		# connect to target
		connsocket.connect((tgthost,tgtPort))
		print "++>> %d UDP OPEN " % tgtPort
		printbanner(connsocket,tgtPort)
	except:
		print "++>> %d UDP CLOSED " % tgtPort
	finally:
		connsocket.close()		


def portscan(tgthost,tgtports,isUdp):
	try:
		tgtIp = gethostbyname(tgthost)
	except:
		print "[--] Error : Unknow Host"
		exit(0)
	try:
		tgtname = gethostbyaddr(tgtIp)
		print "++>> Scan result for :" + tgtname[0] +"....."
	except:
		print "++>> Scan result for :" + tgtIp + "......"
	

	setdefaulttimeout(10)

			#for each port call the conscan funtion to check th port and banner grab
	for tgtPort in tgtports:
		if not isUdp:
			conscanTcp(tgthost,int(tgtPort))
		else:
			conscanUdp(tgthost,int(tgtPort))	

def maintwo():
	# parse the cmd line arguments
	parser = argparse.ArgumentParser('python targetscanner.py')
	parser.add_argument("-a","--address",type=str,help="the target IP address")
	parser.add_argument("-p","--port",type=str,help="the port number to connect with")
	parser.add_argument("-u","--udp",help="Include UDP port Scan",action="store_true")
	args = parser.parse_args()

	# store the arg values
	ipaddress = args.address
	portnum = args.port.split(',')
	isUdp = args.udp

    # POrt scan function
	portscan(ipaddress,portnum,isUdp) 

if __name__ == '__main__':
		maintwo()




