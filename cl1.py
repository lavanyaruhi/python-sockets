import socket 


print("****************************level-1***********************")
host='localhost'
port=235
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((host,port))
msg=input("Enter a msg to send to the server:")
client.send(msg.encode())
response=client.recv(1024).decode()
print(response)
if msg == 'Good Bye':
    print('connection terminated')
    client.close()

