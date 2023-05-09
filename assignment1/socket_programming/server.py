import socket

s=socket.socket()

s.bind(('localhost',12312))

s.listen(1)
print("Waiting for connections")

while True:
    c, addr = s.accept()
    name =c.recv(1024).decode()
    print("Connected with",addr,name)
    c.send(bytes('Welcome to local machine of Ankeet','utf-8'))
    c.sendall(bytes(name,'utf-8'))
    c.close()
