import socket
import threading
import tkinter as tk
from tkinter import scrolledtext, messagebox

# --- Client Configuration ---
HOST = '127.0.0.1'
PORT = 5555

class ChatApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Python Chat")
        self.root.geometry("400x500")
        
        # Connect to Server
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.client_socket.connect((HOST, PORT))
        except:
            messagebox.showerror("Error", "Could not connect to server.")
            self.root.destroy()
            return

        # --- Build the GUI ---
        # Username Input
        self.name_frame = tk.Frame(self.root)
        self.name_frame.pack(pady=10)
        tk.Label(self.name_frame, text="Username:").pack(side=tk.LEFT)
        self.name_entry = tk.Entry(self.name_frame)
        self.name_entry.pack(side=tk.LEFT, padx=5)
        
        # Chat History Box
        self.chat_history = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, state='disabled')
        self.chat_history.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        
        # Message Input Box
        self.msg_frame = tk.Frame(self.root)
        self.msg_frame.pack(padx=10, pady=10, fill=tk.X)
        self.msg_entry = tk.Entry(self.msg_frame)
        self.msg_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
        self.msg_entry.bind("<Return>", self.send_message) # Press Enter to send
        
        self.send_btn = tk.Button(self.msg_frame, text="Send", command=self.send_message)
        self.send_btn.pack(side=tk.RIGHT, padx=5)

        # Start thread to receive messages
        threading.Thread(target=self.receive_messages, daemon=True).start()

    def display_message(self, message):
        """Helper to add text to the chat box."""
        self.chat_history.config(state='normal')
        self.chat_history.insert(tk.END, message + "\n")
        self.chat_history.yview(tk.END) # Scroll to bottom
        self.chat_history.config(state='disabled')

    def send_message(self, event=None):
        name = self.name_entry.get().strip()
        msg = self.msg_entry.get().strip()
        
        if not name:
            messagebox.showwarning("Warning", "Please enter a username first!")
            return
        if msg:
            full_message = f"[{name}]: {msg}"
            self.display_message(f"You: {msg}") # Show own message in UI
            self.client_socket.send(full_message.encode('utf-8'))
            self.msg_entry.delete(0, tk.END) # Clear input box

    def receive_messages(self):
        while True:
            try:
                message = self.client_socket.recv(1024).decode('utf-8')
                if message:
                    self.display_message(message)
            except:
                self.display_message("[Connection to server lost]")
                self.client_socket.close()
                break

if __name__ == "__main__":
    root = tk.Tk()
    app = ChatApp(root)
    root.mainloop()