import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ("Socket created")
print(s)

host = 'www.google.com'
port = 80

remote_ip = socket.gethostbyname( host )
print(remote_ip)

print ('Ip address of ' + host + ' is ' + remote_ip)

s.connect((remote_ip , port))
print ('Socket Connected to ' + host + ' on ip ' + remote_ip)
