import socket
import pickle
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_address = ("127.0.0.1",8000)
client.connect(server_address)
msg = input("Enter message to send: ")
client.send(msg.encode())

def decode(codes):
    table = {i:chr(i) for i in range(256)}
    current_code = 256
   
    current_sequence = chr(codes[0])
    result = [current_sequence]
    for code in codes[1:]:
        if code in table:
            entry = table[code]
        elif code == current_code:
            entry = current_sequence + current_sequence[0]
        else:
            raise ValueError("invalid data")
        result.append(entry)
        table[current_code] = current_sequence+entry[0]
        current_code+=1
        current_sequence=entry
    return ''.join(result)

msg, address = client.recvfrom(1024)
msg = pickle.loads(msg)
print(f"Codes received from Server: {msg}")
print(f"Decoded data: {decode(msg)}")