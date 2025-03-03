import socket
from enum import Enum

class congigParam(Enum):
    ServerClient = 0

 # Define the server address and port
server_ip = '192.168.5.210'  # Localhost
server_port = 7       # Port number on which server is listening

if congigParam(0).value == 1:#Client
   
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    client_socket.connect((server_ip, server_port))

    # Send data to the server
    message = "Hello, This is Aniruddha Patil."
    client_socket.sendall(message.encode('utf-8'))

    while 1:
        # Receive response from the server
        response = client_socket.recv(5)  # Buffer size of 1024 bytes
        print(f"Received from server: {response.decode('utf-8')}")

    # Close the connection
    client_socket.close()

else :#Server

    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the address and port
    server_socket.bind((server_ip, server_port))

    # Start listening for incoming connections
    server_socket.listen(1)
    print(f"Server listening on {server_ip}:{server_port}...")

    # Accept incoming connection
    client_socket, client_address = server_socket.accept()
    print(f"Connection from {client_address} established.")

while 1:
    # Receive data from the client
    data = client_socket.recv(1024)
    print(f"Received from client: {data.decode('utf-8')}")

    # Send response back to the client
    client_socket.sendall(b"Hello, Client! Message received.")

    # Close the client socket and the server socket
client_socket.close()
server_socket.close()    
