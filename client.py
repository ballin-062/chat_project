import socket
import threading
import argparse

def listen_to_server(sock):
    """
    input: takes a socket
    This function uses a while loop to receive data from the chat server, 
    breaking when an exception is thrown.
    """
    try:
        while True:
            data = sock.recv(1024).decode()
            if not data:
                break
            print(data)
    except Exception as e:
        print("Disconnected from server.")
        print(e)
    finally:
        sock.close()

def start_client(host, port):
    """
    input: host and port, specified from the program initialization
    """
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    # create a thread on function "listen_to_server"
    listener = threading.Thread(target=listen_to_server, args=(client_socket,))
    listener.daemon = True
    listener.start()

    # register user with server
    username = input("Enter a username: ")
    client_socket.send(f"server:register {username}".encode())

    # main while loop of program 
    # waiting for user input before sending to server
    while True:
        message = input("->")
        if message.strip().lower() == "server:exit":
            client_socket.send(message.encode())
            break
        client_socket.send(message.encode())

    client_socket.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple Chat Client")
    parser.add_argument("--host", type=str, default="127.0.0.1", help="Server IP")
    parser.add_argument("--port", type=int, default=8080, help="Server Port")
    args = parser.parse_args()

    start_client(args.host, args.port)
