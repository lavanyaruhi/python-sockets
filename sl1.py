import socket

print("***********************level-1***********************")
host='localhost'
port=235
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((host,port))
server.listen()
print('server is listening on {} : {}'.format(host,port))

while True:
    client, client_address = server.accept()
    print('connected to ',client_address)
    msg=client.recv(1024).decode()
    client.send('server received:{}'.format(msg).encode())

    if msg == 'Good Bye':
        print('client diconnected')
        client.close()
        break
server.close()
