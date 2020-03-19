import socket
# get the ip address for the client
hostname = socket.gethostname()
ipaddr = socket.gethostbyname()
port = 6767

# creating a socket connection
s = socket.socket()
# connecting to local host and port
s.connect((ipaddr,port))
# enter the filename to be sent
filename = input('Enter the file name:')
print('sending the file name!!')
s.send(filename.encode())
print('File Name sent!!')
s.close()
# getting contents of the file
s.connect((ipaddr,port))
print('Now the contents of the file will be sent')
content = ''
with open(filename,'rb') as f:
    content += f.read()
    while content:
        s.send(content.encode())
print('The contents of the files are sent!!')
s.close()

