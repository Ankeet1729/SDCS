import socket
import json
import selectors

# Define the IP address and port number for the relay server
HOST = 'localhost'
PORT = 8000

# Create a socket object for the server and bind it to the IP address and port number
select=selectors.DefaultSelector()
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))

# Listen for incoming connections using the listen() method
server_socket.listen()

# Use the select() method to handle multiple clients at once
read_list = [server_socket]
write_list = []
error_list = []

# Define the function to handle push requests
def handle_push(client_socket, dump_server):
    # Receive data from the client
    data = client_socket.recv(1024)

    # Parse the received data to extract the JSON header
    json_header = json.loads(data.decode())
    byteorder = json_header['byteorder']
    length_of_data = json_header['length_of_data']
    request = json_header['request']
    user = json_header.get('user', None)

    # Check if the request is "push"
    if request == 'push':
        # Connect to the dump server
        dump_server.connect(('localhost', 9000))

        # Send data to the dump server
        dump_server.send(data)

        # Receive response from the dump server
        response = dump_server.recv(1024)

        # Send response back to the client
        client_socket.send(response)

        # Close the socket object for the dump server
        dump_server.close()

# Loop indefinitely to accept and handle incoming connections
while True:
    # Use the select() method to handle multiple clients at once
    # read_sockets, write_sockets, error_sockets = select.select((read_list, write_list, error_list))

    for sock in read_sockets:
        # If the server socket is ready to read, accept the incoming connection
        if sock == server_socket:
            client_socket, client_address = server_socket.accept()
            read_list.append(client_socket)
            print(f"Connection established with {client_address}")

        # If a client socket is ready to read, receive data from the client and relay it to the dump server
        else:
            # Create a socket object for the dump server
            dump_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            try:
                handle_push(sock, dump_server)

            except:
                sock.close()
                read_list.remove(sock)
                print(f"Connection closed with {client_address}")
