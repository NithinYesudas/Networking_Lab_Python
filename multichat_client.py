import socket
import threading
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_address = ("127.0.0.1",8000)
client.connect(server_address)

def send():
    while True:
        msg = input()
        client.send(msg.encode())
def receive():
    while True:
        msg, address = client.recvfrom(1024)
        print(msg.decode())
def main():
    send_thread = threading.Thread(target=send)
    receive_thread = threading.Thread(target=receive)
    receive_thread.start()
    send_thread.start()
   
    
main()