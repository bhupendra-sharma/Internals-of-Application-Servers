import json
contract=json.load(open("contract.json"))
file_str='''
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
    msg=json.loads(msg)'''
for i in contract["remote_procedures"]:
    file_str+='''
    if msg['procedure_name'] == "{}":
        res={}('''.format(i['procedure_name'],i["procedure_name"])
    for j in range(0,len(i['parameters'])):
        file_str+="msg['parameters'][{}]['value'],".format(j)
    file_str+=')\n        c.sendall(str(res).encode())'
f=open('rpc_server.py','w+')
f.write(file_str)

