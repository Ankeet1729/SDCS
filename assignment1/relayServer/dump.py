import socket

# Define the IP address and port number for the dump server
HOST = 'localhost'
PORT = 9000

# Create a socket object for the dump server and bind it to the IP address and port number
dump_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dump_server_socket.bind((HOST, PORT))

# Listen for incoming connections using the listen() method
dump_server_socket.listen()

# Loop indefinitely to accept and handle incoming connections
while True:
    # Accept the incoming connection
    client_socket, client_address = dump_server_socket.accept()
    print(f"Connection established with {client_address}")

    # Receive data from the client and send response back
    data = client_socket.recv(1024)
    response = b"Data received successfully"
    client_socket.send(response)

    # Close the socket object for the client
    client_socket.close()
    print(f"Connection closed with {client_address}")
