
import json
import socket
def send_to_server(msg):
    port=5001
    host="localhost"
    s=socket.socket()
    s.connect((host,port))
    json_msg=json.dumps(msg)
    s.sendall(json_msg.encode())
    return s.recv(1024).decode()


def foo(par_1,):
    msg=dict()
    msg["procedure_name"]="foo"
    msg["parameters"]=list()
    msg["return_type"]="string"
    msg['parameters'].append({'parameter_name':'par_1','data_type':'int','value':par_1})
    resp=send_to_server(msg)
    if msg['return_type'] == "void":
        return None
    return str(resp)
    
def bar(par_1,par_2,):
    msg=dict()
    msg["procedure_name"]="bar"
    msg["parameters"]=list()
    msg["return_type"]="int"
    msg['parameters'].append({'parameter_name':'par_1','data_type':'int','value':par_1})
    msg['parameters'].append({'parameter_name':'par_2','data_type':'string','value':par_2})
    resp=send_to_server(msg)
    if msg['return_type'] == "void":
        return None
    return int(resp)
    
def upperCase(par_1,):
    msg=dict()
    msg["procedure_name"]="upperCase"
    msg["parameters"]=list()
    msg["return_type"]="string"
    msg['parameters'].append({'parameter_name':'par_1','data_type':'str','value':par_1})
    resp=send_to_server(msg)
    if msg['return_type'] == "void":
        return None
    return str(resp)
    
def setName(par_1,):
    msg=dict()
    msg["procedure_name"]="setName"
    msg["parameters"]=list()
    msg["return_type"]="void"
    msg['parameters'].append({'parameter_name':'par_1','data_type':'str','value':par_1})
    resp=send_to_server(msg)
    if msg['return_type'] == "void":
        return None
    return str(resp)
    