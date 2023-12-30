import socket
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_address = ("127.0.0.1",8000)
server.bind(server_address)
server.listen(5)
client, client_address =server.accept()
print(client_address)
while True:
    message, address = client.recvfrom(1024)
    print(message.decode())