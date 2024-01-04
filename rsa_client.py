import socket
import pickle
server_address = ("127.0.0.1",8000)
client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect(server_address)
msg = input("Enter msg to send: ")

#key generation
p = 11
q = 7
n = p*q
phi_n = (p-1)*(q-1)
e = 7
d = pow(e,-1,phi_n)

#send to server
encryption_key = pickle.dumps((e,n))
client_socket.send(encryption_key)
client_socket.send(msg.encode())
data = client_socket.recv(1024)
encryption_msg = data.decode()
print(f"Encryption Message: {encryption_msg}")

#decryption
decrypted_msg = pow(int(encryption_msg),d,n)
print(f"Decrypted message: {decrypted_msg}")

client_socket.close()