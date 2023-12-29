import socket
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_address = ("127.0.0.1",8000)
client.connect(server_address)
while True:
    
    message = input("Enter message to server: ")
    client.send(message.encode())
