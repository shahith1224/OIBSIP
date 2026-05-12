import socket
import threading
import sys

# --- Client Configuration ---
# Must match the server's HOST and PORT
HOST = '127.0.0.1' 
PORT = 5555

def receive_messages(client_socket):
    """Listens for incoming messages from the server."""
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(f"\n{message}")
            else:
                # Empty message means server disconnected
                print("Disconnected from server.")
                break
        except:
            print("An error occurred!")
            client_socket.close()
            break

def start_client():
    """Connects to the server and handles user input."""
    # Ask for the user's name
    name = input("Enter your chat name: ")
    
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect((HOST, PORT))
        print("Connected to the chat server! You can start typing messages.")
    except ConnectionRefusedError:
        print("Could not connect to the server. Is it running?")
        sys.exit()

    # Start a background thread to listen for messages
    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.start()

    # Main thread handles sending messages
    while True:
        message_text = input("")
        if message_text.lower() == 'quit':
            client_socket.close()
            break
            
        full_message = f"[{name}]: {message_text}"
        client_socket.send(full_message.encode('utf-8'))

if __name__ == "__main__":
    start_client()