import socket  
import sys
if len(sys.argv)!=2:
    exit('Invalid arguments,Please enter Port number')
port=int(sys.argv[1])
host=socket.gethostname()
s = socket.socket()
s.connect((host, port))
ip=socket.gethostbyname(host)
while True:
    msg=input('Enter Message:')
    if msg=='quit':
        s.close() 
        break
    s.sendall((str(ip)+":"+str(port)+"%"+msg).encode())
    print("Message from Server:"+s.recv(1024).decode())