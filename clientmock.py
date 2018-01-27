import socket


sock = socket.socket()
sock.connect(('', 9090))

sock.sendall(b'hello world')

data = sock.recv(1024)
