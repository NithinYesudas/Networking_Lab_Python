import socket
import pickle
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_address = ('127.0.0.1',8000)
server.bind(server_address)
server.listen()
client,address = server.accept()


def compress(msg):
    table = {chr(i):i for i in range(256)}
    p = msg[0]
    output_codes = []
    code = 256
    for i in range(len(msg)):
        if i != len(msg) -1:
            c = msg[i+1]
        if p+c in table:
            p = p+c
        else:
            output_codes.append(table[p])
            table[p+c] = code
            code+=1
            p = c
        c=''
    output_codes.append(table[p])
    print(output_codes)
    msg = pickle.dumps(output_codes)
    client.send(msg)
msg,address = client.recvfrom(1024)
msg = msg.decode()
compress(msg)
