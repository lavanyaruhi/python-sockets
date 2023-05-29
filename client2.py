import socket

# create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()
host='127.0.0.1'
port = 8000

# connect to the server
client_socket.connect((host, port))

# receive a welcome message from the server
welcome_message = client_socket.recv(1024).decode('utf-8')
print(welcome_message)

while True:
    # send data to the server
    data = input("Enter a message to send to the server: ")
    client_socket.send(data.encode('utf-8'))
    
    # check if the user wants to disconnect
    if data.strip().lower() == 'bye':
        break
    
    # receive a response from the server
    response = client_socket.recv(1024).decode('utf-8')
    print(response)

# close the client socket
client_socket.close()
