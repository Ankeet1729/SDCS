import socket
import json

# Define the IP address and port number for the server
HOST = 'localhost'
PORT = 8000

# Create a socket object for the client and connect it to the IP address and port number of the server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

# Define the data to be sent to the server
data = {'byteorder': 'little', 'length_of_data': 10, 'request': 'push', 'user': 'John Doe'}
json_header = json.dumps(data).encode()
message = json_header + b'This is the data'

# Send the data to the server
client_socket.send(message)

# Receive response from the server
response = client_socket.recv(1024)

# Print the response
print(response.decode())

# Close the socket object for the client
client_socket.close()
