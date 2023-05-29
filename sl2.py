import socket
print("****************************level-2***********************")
host='localhost'
port=2357
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((host,port))
server.listen()
print('server is listening on {} : {}'.format(host,port))
while True:
    client,client_address=server.accept()
    print('connected to', client_address)
    with open('received.txt','wb') as file:
        while True:
            data=client.recv(1024)
            if not data:
                break
            file.write(data)
            
    print('file received successfully')
    
    client.send('server recived the file' .encode())
    client.close()
    break
server.close()