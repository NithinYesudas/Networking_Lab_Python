import socket
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(("127.0.0.1",8000))

server.listen(1)
client, clientAddress = server.accept()
username,clientAddress = client.recvfrom(1024)
username = username.decode()
print(f"Connection estabilished with: {username}")
while True:
    message, clientAddress = client.recvfrom(1024)
    print(f'{username}: {message.decode()}')
    sent = input("Server: ")
    client.send(sent.encode())
    