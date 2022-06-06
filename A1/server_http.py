import socket
import sys 
if len(sys.argv)!=2:
    exit('Invalid arguments,Please enter Port number')
port=int(sys.argv[1])   
host=socket.gethostname()
s = socket.socket()
s.bind((host, port))
s.listen(2)
while True:
   c, addr = s.accept()
   msg=str(c.recv(1024).decode('ascii'))
   client,msg=msg.split('%')
   while msg != "quit":
      print("Message from Client",client,"->"+msg)
      if str=='quit':
          c.close() 
          break
      c_msg=input("Enter Response:")
      c.sendall(c_msg.encode())
      msg=str(c.recv(1024).decode('ascii'))
   