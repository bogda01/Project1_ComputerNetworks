import socket
from datetime import datetime

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.bind(('127.0.0.1', 8081))
sock.listen()
conn, addr = sock.accept()

with conn:
    print(addr, 'connected')
    conn.send('You are now connected.\n')
    data = conn.recv(1024)
    print('Received message: '+data.decode('utf-8'))

    data = conn.recv(1024)
    conn.send(b'Hi ' + data)

    while True:
        can_answer = False
        data = conn.recv(1024)
        if not data:
            break
        print('Received message:', data.decode('utf-8'))
        if data.decode('utf-8').upper() == 'GOODBYE':
            conn.send(b'goodbye')
            can_answer = True
            break
        if data.decode('utf-8').upper() == 'WHAT IS YOUR NAME?':
            conn.send(b'chaty')
            can_answer = True
        if data.decode('utf-8').upper() == 'WHAT IS THE TIME?':
            now = datetime.now()
            date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
            date_time = date_time.encode()
            conn.send(b'' + date_time)
            can_answer = True
        if data.decode('utf-8').upper() == 'HELLO':
            conn.send(b'Hi!')
            can_answer = True
        if data.decode('utf-8').upper() == 'HOW ARE YOU?':
            conn.send(b'Im good!')
            can_answer = True

        if not can_answer:
            conn.send(b'Im not smart enough')