import socket
import pickle

server_address=("127.0.0.5",8004)
client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect(server_address)

msg=input("Enter msg to send:")

p=11
q=7
n=p*q
phi_n=(p-1)*(q-1)
e=0
g=0

d=1
e=7
while d*e % phi_n >1:
	d+=1

encryption_key=pickle.dumps((e,n,msg))
client_socket.send(encryption_key)

data=client_socket.recv(1024).decode()
print(f"Encrypted Message received from server: {data}")
res=""
for char in data:
	a = pow(ord(char),d,n)
	res+=chr(a+65)
print(f"Decrypted Message: {res}")

client_socket.close()