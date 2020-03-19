import socket
import os
hostname = socket.gethostname()
ipaddr = socket.gethostbyname()
port = 6767
# creating a socket
s = socket.socket()
# binding the socket
s.bind((ipaddr,port))
# listening / waiting for the connection to be established
s.listen(1)
# getting the details of the client
conn,addr = s.accept()
print('A client is connected to the connection!!')
print('This is the IP address of the client:',addr)
# recieving the file name by the client
fname = conn.recv()
#converting the file name to string
fname = conn.recv(fname.decode())
print('File name recieved by the client',fname)
conn.close()
# recieving the contents of the file
# creating  a new connection
conn,addr = s.accept()
print('A client is connected to the connection!!')
print('This is the IP address of the client:',addr)

fcontent=''
while conn:
    fcontent = conn.recv(bufsize=1024)
    fcontent += str(fcontent.decode())

if fcontent=='':
    print('No file recieved!!')
# creating a file with same name 
else:
    if os.path.isfile(fname):
        fname = input('File with this name already exists please input a new name:')
        with open(fname,'wb') as f:
            f.write(fcontent)
    else:
        with open(fname,'wb') as f:
            f.write(fcontent)
    print('File copied Successfully!!')
conn.close()
