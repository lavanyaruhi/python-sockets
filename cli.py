import socket

s = socket.socket()

p = "127.0.0.1"
port = 8888
D_name = socket.gethostname()
ip = socket.gethostbyname(D_name)
print(ip)
s.connect(( p,port ))
# import server100

while True:
    output = input("enter msg")
    # while (output != 'end'):
    s.send(output.encode())
    msg=s.recv(1024)
    reply=msg.decode()
    print(reply)
    #response = []
    #response.append(reply)
    #for i in response:
     #   print(response[i],i)
    #string = storedstrings[ci]
    #string=reply
    #for i, string in enumerate(reply,start=1):
     #   print(i, string)
    #for i, string in enumerate(storedstrings, start=1):
     #   print(i, string)






"""import socket


def send_request(host, port):
    s=socket.socket()
    s.connect((host,port))
    message='Hello, server!'
    s.sendall(message.encode())
    
    data=s.recv(1024)
    print(f'received response: {data.decode()}')
    s.close()
    
if __name__=='__main__':
    hosts=['127.0.0.1','127.0.0.2']
    ports=[8000,8001]
    for i in range(len(hosts)):
        send_request(hosts[i], ports[i])"""
