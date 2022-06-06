import json
contract=json.load(open("contract.json"))
f=open("rpc_client.py","w+")
file_str='''
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

'''
func_str='''
def {}({}):
    msg=dict()
    msg["procedure_name"]="{}"
    msg["parameters"]=list()
    msg["return_type"]="{}"'''
for i in contract["remote_procedures"]:
    parameters=""
    for j in i["parameters"]:
        parameters+=j["parameter_name"]+','
    file_str=file_str+func_str.format(i["procedure_name"],parameters,i["procedure_name"],i["return_type"])
    for j in i["parameters"]:
        file_str+="\n    msg['parameters'].append({{'parameter_name':'{}','data_type':'{}','value':{}}})".format(j["parameter_name"],j["data_type"],j["parameter_name"])
    file_str+='''
    resp=send_to_server(msg)
    if msg['return_type'] == "void":
        return None
    return {}(resp)
    '''.format("str" if i['return_type']=="string" or i['return_type']=="void"  else i['return_type'])
# print(file_str)
f.write(file_str)