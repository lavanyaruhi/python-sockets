import socket

# create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()
host='127.0.0.1'
port = 8000

# bind the socket to a public host, and a well-known port
server_socket.bind((host, port))

# become a server socket
server_socket.listen(5)

print("Server is listening on {}:{}".format(host, port))

# create an empty list to hold the connected clients
clients = []

while True:
    # establish a connection
    client_socket, addr = server_socket.accept()
    print('Got a connection from {}'.format(addr))
    
    # add the new client to the clients list
    clients.append(client_socket)
    
    # send a welcome message to the client
    message = "Welcome to the server!"
    client_socket.send(message.encode('utf-8'))
    
    while True:
        # receive data from the client
        data = client_socket.recv(1024).decode('utf-8')
        print('Received data from client: {}'.format(data))
        
        # check if the client sent a "bye" message
        if data.strip().lower() == 'bye':
            # remove the client from the clients list
            clients.remove(client_socket)
            print('Client disconnected: {}'.format(addr))
            client_socket.close()
            break
        
        # send a response to all connected clients except the sender
        response = "Received your message: {}".format(data)
        for c in clients:
            if c != client_socket:
                c.send(response.encode('utf-8'))
