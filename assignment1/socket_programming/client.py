import socket

c=socket.socket()

c.connect(('127.0.0.1',12312))
name=input("Enter Name")
c.send(bytes(name,'utf-8'))
print(c.recv(1024).decode())