import socket
import threading
import pickle


def serve_client(sock, connection, address):
    print('serving client')
    while True:
        try:
            data = conn.recv(1024 * 2 * 2 * 2)
            print(data)
            if not data:
                break

        except socket.error:
            pass


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 9090))

sock.listen(5)

while True:
    conn, address = sock.accept()
    print(conn, address)
    my_thread = threading.Thread(target=serve_client, args=(sock, conn, address))
    my_thread.start()
