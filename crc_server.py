import socket
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_address = ('127.0.0.1',8000)
key= '1101'
server.bind(server_address)
server.listen()
print(f"Server listening on: {server_address}")
client, address = server.accept()
encoded_msg,address = client.recvfrom(1024)
msg = encoded_msg.decode()
def xor(dividend,divisor):
    result = ''
    for i in range(1,len(dividend)):
        if(dividend[i]==divisor[i]):
            result=result+'0'
        else:
            result= result+'1'
    
    return result
def mod2div(msg):
    length = len(key)
    temp = msg[0: length]
    while length < len(msg):
        if temp[0] == '1':
            temp = xor(temp,key)+msg[length]
        else:
            temp = xor(temp,'0'*length)+msg[length]
        length+=1
    if temp[0] == '1':
        temp = xor(temp,key)
    else:
        temp = xor(temp,'0'*length)
    return temp
def decode():
    reminder = mod2div(msg)
    print(reminder)
    if reminder == '000':
        print("No error found")
    else: 
        print("Error found")

decode()