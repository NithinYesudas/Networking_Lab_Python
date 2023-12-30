import socket
client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_address = ("127.0.0.1",8000)
client_socket.connect(server_address)
key = "1101"



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
    send = msg[0: length]
    while length<len(msg):
        if send[0]=='1':
            send = xor(send,key) + msg[length]
        else:
            send = xor(send,'0'*length) + msg[length]
        length+=1
    
    if send[0]=='1':
        send = xor(send,key)
    else:
        send = xor(send,'0'*length)
    temp = send 
    
    return temp
    
      
    
def encode(msg):
    padded_message =msg+'0'*(len(key)-1)
    reminder = mod2div(padded_message)
    return msg+reminder

def main():
    msg = input("Enter the binary message: ")
    msg = encode(msg)
    client_socket.send(msg.encode())
main()