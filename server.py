import socket

# getting the ip address of the host by getting the host name and using it to get the ip address
hostname = socket.gethostname()
ipaddr = socket.gethostbyname(hostname)

# create a socket for tcp/ip communication
s = socket.socket()
# binding the post and the host ip address
port= 9999
s.bind((ipaddr,port))
print('binded and listening!!')
# listening 
s.listen()
# waithing for the connection to be accepted
conn,addr = s.accept()
# getting the details of host to which we are connected
print('Connected to host ip address:',addr)
#sending the messages to the client
conn.send(b'Hi my name is harsh here!!')
# other way to encode
msg = str.encode('Hello dont u remeber kamlesh!!')
conn.send(msg)

# after the chat is over close the connection
conn.close()
