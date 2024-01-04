import socket
client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_address = ("127.0.0.1",8000)
client_socket.connect(server_address)
key = "1101"
def xor(a,b):
    result=''
    for i in range(1,len(a)):
        if a[i]==b[i]:
            result = result+'0'
        else:
            result = result+'1'
    return result
        
def mod2div(msg):
    length = len(key)
    temp = msg[0:length]
    while length < len(msg):
        if temp[0] == '1':
            temp = xor(temp,key) + msg[length]
        else:
            temp = xor(temp,'0'*length) + msg[length]
        length+=1
    if temp[0] == '1':
        temp = xor(temp,key) 
    else:
        temp = xor(temp,'0'*length) 
    return temp
        
    
def encode(msg):
    padded_msg = msg+'0'*(len(key)-1)
    reminder = mod2div(padded_msg)
    return msg+reminder

def main():
    msg = input("Enter a binary string: ")
    msg = encode(msg)
    client_socket.send(msg.encode())
    client_socket.close()
main()