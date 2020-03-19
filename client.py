import socket

# getting the ip address of the host
hostname = socket.gethostname()
ipaddr = socket.gethostbyname(hostname)
# creating a socket object 
s = socket.socket()
# connecting to the port
s.connect((ipaddr,port))

# getting the message
msg = s.recv(1024)

while msg:
    print('message recieved:',msg.decode())
    msg = s.recv(1024)
s.close()