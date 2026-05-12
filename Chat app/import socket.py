import socket
import threading

# --- Server Configuration ---
HOST = '127.0.0.1' # Localhost (runs on your own machine)
PORT = 5555        # Port to listen on

# List to keep track of connected clients
clients = []

def broadcast(message, sender_client):
    """Sends a message to all connected clients except the sender."""
    for client in clients:
        if client != sender_client:
            try:
                client.send(message)
            except:
                # Remove client if unable to send a message
                clients.remove(client)

def handle_client(client, address):
    """Handles incoming messages from a single client."""
    print(f"[NEW CONNECTION] {address} connected.")
    
    while True:
        try:
            # Receive message from the client
            message = client.recv(1024)
            if not message:
                break
            
            # Broadcast it to everyone else
            broadcast(message, client)
        except:
            # If an error occurs (e.g., client disconnects abruptly)
            break
            
    print(f"[DISCONNECTED] {address} disconnected.")
    clients.remove(client)
    client.close()

def start_server():
    """Starts the server and listens for connections."""
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    print(f"[STARTING] Server is listening on {HOST}:{PORT}")
    
    while True:
        # Accept a new client connection
        client, address = server.accept()
        clients.append(client)
        
        # Start a new thread to handle this specific client
        thread = threading.Thread(target=handle_client, args=(client, address))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

if __name__ == "__main__":
    start_server()