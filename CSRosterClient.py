import socket

ClientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ClientSocket.connect(("192.168.56.1", 1337))

while True:
    msg = ClientSocket.recv(4096)
    print(msg.decode("utf-8"))