import socket
server_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server_address = ("127.0.0.2",8000)
server_socket.bind(server_address)
print(f"Server listening on: {server_address}")
message = "received"
try:
    while True:
        data, client_address = server_socket.recvfrom(1024)
        print(data.decode())
        server_socket.sendto(message.encode(),client_address)
except KeyboardInterrupt():
    server_socket.close()
    exit()