import socket

HOST = '127.0.0.1'
PORT = 12345


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    choice1 = input('Enter choice 1: ')
    choice2 = input('Enter choice 2: ')
    choice3 = input('Enter choice 3: ')
    choices = ','.join([choice1, choice2, choice3])
    s.sendall(choices.encode())
    data = s.recv(1024).decode()
    print('The correct choice is:', data)