import socket
from _thread import *

s=socket.socket()
ip=socket.gethostbyname(socket.gethostname())
port=8888
p="127.0.0.1"
s.bind((p,port))
s.listen(10)

print('server is listening')
noOfclients=0
names = []
def client(conn):
    while True:

        # conn, address = s.accept()
        data = conn.recv(1024)
        data = data.decode()
        names.append(data)
        m=''
        for i in names:
            m+=i
            m+='  '
        conn.send(m.encode())
        # print(data)

def nameinlist():
    for i in names:
        conn.send(i.encode("utf=8"))

# nameinlist()


while True:
    conn, address = s.accept()
    start_new_thread(client,(conn,))
    noOfclients += 1
    print('client', noOfclients, 'host')
    print('connected client is :', address)






"""import socket
import threading

def handle_client(conn,addr):
	print(f'new connection from {addr}')
	data=conn.recv(1024)
	print(f'received data: {data.decode()}')
	response='Hello, client'
	conn.sendall(response.encode())
	conn.close()
	print(f'connection with {addr} closed')
	
	
def start_server(host,port):
	s=socket.socket()
	s.bind((host,port))
	s.listen()
	print(f'server is listening on {host}:{port}')
	while True:
		conn, addr = s.accept()
		client_thread=threading.Thread(target=handle_client, args=(conn, addr))
		client_thread.start()
if __name__=='__main__':
	host=['127.0.0.1','127.0.0.2']
	port = [8000, 8001]
	for i in range(len(host)):
        server_thread=threading.Thread(target=start_server, args=(host[i],port[i]))
        server_thread.start()"""
    