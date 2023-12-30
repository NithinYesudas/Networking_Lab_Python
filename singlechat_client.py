import socket
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_address = ("127.0.0.1",8000)
client.connect(server_address)
username = input("Enter your name: ")
client.send(username.encode())
while True:
    message = input(f'{username}: ')
    client.send(message.encode())
    data, server = client.recvfrom(1024)
    print(f"Server: {data.decode()}")
    