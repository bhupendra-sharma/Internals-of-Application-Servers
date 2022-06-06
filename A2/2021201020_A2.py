import sys
import socket
import ssl
def isvalidURL(s):
    return True

if len(sys.argv)!=2:
    exit("Please provide url.")
url=sys.argv[1]
if(isvalidURL(url)==False):
    exit("Please provide correct url")
ip=socket.gethostbyname(url)
# print(url,":",ip)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((url, 443))
s = ssl.wrap_socket(s, keyfile=None, certfile=None, server_side=False, cert_reqs=ssl.CERT_NONE, ssl_version=ssl.PROTOCOL_SSLv23)
# msg = "GET / HTTP/1.1\r\n\r\n"
msg = "GET / HTTP/1.1\r\nHost: {}\r\nConnection: close\r\n\r\n".format(url)
s.send(msg.encode())
resp=s.recv(4096).decode()
final_content=""
while  resp:
    final_content=final_content+(resp)
    resp=s.recv(4096).decode()

# if header_data.
print(final_content)