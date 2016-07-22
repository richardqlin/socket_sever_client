import socket                   # Import socket module

host='127.0.0.1'
port = 6000                    # Reserve a port for your service.
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))

while 1:
	Input=input('Input from client2: ')
	s.send((Input+' from client 2').encode())
	reserver_data=s.recv(1024)
	print ('Received from server:',reserver_data)

s.close()

