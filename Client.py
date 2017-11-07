import socket

s=socket.socket()
host=socket.gethostname()
port=1234

s.connect((host,port))

while True:
	mes=s.recv(1024)
	print mes 
	if(mes=="Server says Bye" or mes=='bye'):
		s.sendall("Bye")
		break
	x=raw_input("Enter: ")	
	s.send(x)
s.close()	
