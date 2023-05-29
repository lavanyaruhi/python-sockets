import socket


print("****************************level-2************************")
host='localhost'
port=2357
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((host,port))
with open('sendfile.txt','rb')as file1:
    while True:
        data=file1.read(1024)
        if not data:
            break
        client.send(data)

response=client.recv(1024).decode()
print(response)
client.close()