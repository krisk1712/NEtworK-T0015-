 import socket 
 import threaading
 import argparse

 def serverClient(clientToServerSocket,clientIPAddress,portnum):
 	clientRequest = clientToServerSocket.recv(4096)
 	print "++>> Recived data from the client (%s:%d) " % (clientIPAddress,portnum,clientRequest)
 	clientToServerSocket.send("I am a server responese")
 	clientToServerSocket.close() 
 


 def startServer(portnum):
 	server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
 	server.bind(("0.0.0.0",portnum))
 	server.listen(10)
 	print "++>> Listening Locally on port %d " portnum


 	while True:
 		client,address = server.accept()
 		print "++>> Connect with the client %s: %d " % (address[0],address[1])

 		serverClientThread = threaading.Thread(target=serverClient,args=(client,address[0],address[1]))
 		serverClientThread.start()




 def mainfour():
 	parser = argparse.ArgumentParser('Tcp Server')
 	parser.add_argument("-p","--port",type=int,help="The port to connect",default=4444)
 	args = parser.parse_args()

 	# store
 	portnum = args.port

 	startServer(portnum)



 if __name__ == '__main__':
 		mainfour()	