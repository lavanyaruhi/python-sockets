import socket
import threading

def handle_client(client_socket):
	while True:
		data = client_socket.recv(1024)
		if not data:
			break
		respone='you sent:'+data.decode()
		client_socket.send(respone.encode())
	client_socket.close()
def start_server():
	server_socket=socket.socket()
	server_address=('localhost',5656)
	server_socket.bind(server_address)
	server_socket.listen(5)
	print('server is listening on {}:{}'.format(server_address[0],server_address[1]))
	
    
	while True:
		client_socket,client_address=server_socket.accept()
		print('new client connected: {}:{}'.format(client_address[0],client_address[1]))
		client_thread=threading.Thread(target=handle_client, args=(client_socket,))
		client_thread.start()
		
if __name__=='__main__':
	start_server()