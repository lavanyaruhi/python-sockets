import socket

def get_correct_choice(choices):
    return choices[0]

HOST = '127.0.0.1'
PORT = 12345


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    
    s.bind((HOST, PORT))
    s.listen()

    print('Server is listening on port', PORT)

    while True:
        conn, addr = s.accept()
        print('Connected by', addr)
        data = conn.recv(1024).decode()
        choices = data.split(',')
        correct_choice = get_correct_choice(choices)
        conn.sendall(correct_choice.encode())
        conn.close()