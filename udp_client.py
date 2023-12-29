import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ("127.0.0.2",8000)
try: 
    while True:
        message = input("Enter message to server: ")
        client_socket.sendto(message.encode(), server_address)
        data, address = client_socket.recvfrom(1024)
        print(data.decode())
        if data.decode() == "received":
            break
except KeyboardInterrupt():
    client_socket.close()
    exit()
