import socket

s=socket.socket()
host=socket.gethostname()
port=1234
s.bind((host,port))

s.listen(1)
c,add=s.accept()
while True:
    mes=raw_input("Enter: ")
    c.send(mes)
    x=c.recv(1024)
    if x=='Bye':
		print x
		break
c.send("Server says Bye")		
c.close()

