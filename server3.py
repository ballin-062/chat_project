import socket
import threading
import argparse

# Store active users: {username: socket}
active_users = {}
lock = threading.Lock()

def handle_client(client_socket, address):
    username = None
    try:
        while True:
            message = client_socket.recv(1024).decode()
            if not message:
                break

            if message.startswith("server:register "):
                requested_name = message.split(" ", 1)[1].strip()
                with lock:
                    if requested_name in active_users:
                        client_socket.send("server: Username already taken.\n".encode())
                    else:
                        username = requested_name
                        active_users[username] = client_socket
                        client_socket.send(f"server: Registered as {username}.\n".encode())

            elif message == "server:who":
                with lock:
                    user_list = "Online Users: " + ", ".join(active_users.keys()) + "\n"
                client_socket.send(user_list.encode())

            elif message == "server:exit":
                client_socket.send("server: Goodbye!\n".encode())
                break

            elif ":" in message:
                recipient, msg = message.split(":", 1)
                with lock:
                    if recipient in active_users:
                        active_users[recipient].send(f"From {username}: {msg}".encode())
                    else:
                        client_socket.send("server: Recipient not found.\n".encode())
            else:
                client_socket.send("server: Unknown command or bad format.\n".encode())

    except Exception as e:
        print(f"Error with {address}: {e}")
    finally:
        with lock:
            if username and username in active_users:
                del active_users[username]
        client_socket.close()
        print(f"{address} disconnected.")

def start_server(port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', port))
    server_socket.listen(5)
    print(f"Server listening on port {port}...")

    try:
        while True:
            client_socket, address = server_socket.accept()
            print(f"Connection from {address}")
            thread = threading.Thread(target=handle_client, args=(client_socket, address))
            thread.start()
    except KeyboardInterrupt:
        print("Shutting down server.")
    finally:
        server_socket.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple Chat Server")
    parser.add_argument("--port", type=int, default=8080, help="Port number to listen on")
    args = parser.parse_args()

    start_server(args.port)
