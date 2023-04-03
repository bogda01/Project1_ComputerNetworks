import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

if len(sys.argv) < 3:
    print("Usage: python client.py <server_ip_address> <server_port_number>")
    sys.exit(1)

server_address = (sys.argv[1], int(sys.argv[2]))
print(str(sys.argv[1])+' '+str(sys.argv[2]))

sock.connect(server_address)
sock.send(b'Hello, server!')
data = sock.recv(1024)

print('Received:', data.decode('utf-8'))

print('Enter your name:')

while True:
    text = input()
    textByte = str.encode(text)
    if text.upper() == 'STOP':
        break
    sock.send(textByte)

    data = sock.recv(1024)
    print('Received:', data.decode('utf-8'))

    if data.decode('utf-8').upper() == 'EXIT':
        break

sock.close()
