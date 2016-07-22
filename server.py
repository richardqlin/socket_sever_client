import socket                   # Import socket module
import time
import os

from threading import Thread
host='127.0.0.1'
port = 6000            # Reserve a port for your service.
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))
s.listen(5)
def clientThread():
    conn,addr=s.accept()
    print('Got connection from', addr)
    while 1:
            #conn,addr=s.accept()
            #print('Got connection from', addr)
            data=conn.recv(1024)
            print('get data',data)
            if not data:
                time.sleep(1)
                break
            #os.system(data)
            
            #print(result)
            conn.sendall(data.upper())
def myfunc(i):
    print('sleeping 5 sec from thread',i)
    time.sleep(1)
    print ('finished sleeping from thread',i)

for i in range(5):
    t=Thread(target=clientThread)
    t.start()
#Thread(target=clientThread).start()
s.close()


