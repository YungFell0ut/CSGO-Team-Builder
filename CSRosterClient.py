import socket

ClientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ClientSocket.connect(("IP_ADDRESS", 1337))

while True:
    msg = ClientSocket.recv(4096)
    print(msg.decode("utf-8"))
