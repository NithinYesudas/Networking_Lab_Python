import socket
import pickle
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_address = ("127.0.0.1",8000)
client.connect(server_address)
msg = input("Enter message to send: ")
client.send(msg.encode())

def decode(codes):

    table = {i:chr(i) for i in range(256)}
    p = chr(codes[0])
    current_code = 256
    result= [p]
    for code in codes[1:]:
        if code in table:
           c = table[code]
        elif code == current_code:
            c = p + p[0]
        else:
            raise ValueError("Invalid data")
        result.append(c)
        table[current_code] = p + c[0]
        current_code+=1
        p = c
        
    return ''.join(result)

msg, address = client.recvfrom(1024)
msg = pickle.loads(msg)
print(f"Codes received from Server: {msg}")
print(f"Decoded data: {decode(msg)}")