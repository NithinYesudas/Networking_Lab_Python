import socket
import pickle
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_address = ("127.0.0.5",8004)
server_socket.bind(server_address)
server_socket.listen(5)
print(f"Server listening on: {server_address}")
client_socket, client_address = server_socket.accept()

key=client_socket.recv(1024)
e,n,msg=pickle.loads(key)

print("Message to be encrypted: ",msg)
result=""
for char in msg:
	encrypted_msg=pow(ord(char)-ord('A'),e,n)
	result+=chr(encrypted_msg)

print(f"Encrypted message: {result}")
client_socket.send(result.encode())

client_socket.close()
server_socket.close()