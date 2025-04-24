# 🗨️ Simple Python Chat Application

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Platform](https://img.shields.io/badge/Platform-Cross--Platform-brightgreen)
![Status](https://img.shields.io/badge/Status-Active-success)
![License](https://img.shields.io/badge/License-MIT-green)


This is a basic **TCP-based chat application** written in Python. It includes a client and server script, allowing multiple users to connect and exchange messages in real time via the command line.

---

## 🚀 Features

- Lightweight and simple to use
- TCP socket-based communication
- Custom host and port configuration
- Easily extendable for encryption, GUIs, or group chat features

---

## 🛠️ Usage

### ✅ Start the Server

```bash
$ python server.py --port <port#>
```
Example:

```bash
$ python server.py --port 5000
```
### ✅ Start a Client
```bash
$ python client.py --host <IP> --port <port#>
```
### Example:

```bash
$ python client.py --host 127.0.0.1 --port 5000
```
You can run the server and multiple clients on the same machine using different terminals, or across different machines on the same network.

🖼️ Screenshots
You can showcase how the client looks in action here. Upload your screenshots to the assets/ folder (or wherever you prefer), and update the paths below:

🧑‍💻 Client Terminal Example

📁 File Structure

```yaml
chat-app/
├── client.py
├── server.py
├── README.md
└── assets/
    └── client_example.png  # (Add your screenshots here)
```
📌 To-Do / Future Features
 Add support for usernames/nicknames/aliases

 Add group chat or broadcast system

 Implement message encryption (SSL or RSA)

 Build a simple GUI using Tkinter or PyQt

🧙🏽‍♂️ Author
Created by Colin Torbett.
Feel free to fork, use, and improve this tool for learning or development.

📜 License
This project is licensed under the MIT License.
---

Let me know if you’d like to:
- Add emoji or badge flair 🌟
- Automatically log messages to a file 📄
- Write a simple test script for this app 🧪

Happy coding!