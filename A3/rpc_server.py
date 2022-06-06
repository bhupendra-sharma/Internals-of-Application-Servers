
import socket
import json
from server import *
port=5001  
host="localhost"
s = socket.socket()
s.bind((host, port))
s.listen(4)
while True:
    c, addr = s.accept()
    msg=c.recv(1024).decode()
    msg=json.loads(msg)
    if msg['procedure_name'] == "foo":
        res=foo(msg['parameters'][0]['value'],)
        c.sendall(str(res).encode())
    if msg['procedure_name'] == "bar":
        res=bar(msg['parameters'][0]['value'],msg['parameters'][1]['value'],)
        c.sendall(str(res).encode())
    if msg['procedure_name'] == "upperCase":
        res=upperCase(msg['parameters'][0]['value'],)
        c.sendall(str(res).encode())
    if msg['procedure_name'] == "setName":
        res=setName(msg['parameters'][0]['value'],)
        c.sendall(str(res).encode())