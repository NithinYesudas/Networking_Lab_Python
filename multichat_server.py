import socket
import threading
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_address = ("127.0.0.1",8000)
server.bind(server_address)
server.listen(5)
print(f"Server listening on: {server_address}")
clients = {}
def handle_clients():
    while True:
        client_socket, client_address = server.accept()
        print(f"Connection estabilished with: {client_address}")
        broadcast(f"{client_address} has joined the chat")
        name = f"User{len(clients) + 1}"
        clients[name] = client_socket
        thread = threading.Thread(target=handle_client,args=(client_socket,name))
        thread.start()
        
def handle_client(client_socket, name):
    while True:
        msg, address = client_socket.recvfrom(1024)
        print(f"{name}: {msg.decode()}")  
        broadcast(f"{name}: {msg.decode()}") 
def broadcast(msg):
    for client in clients.values():
        client.send(msg.encode())

handle_clients()