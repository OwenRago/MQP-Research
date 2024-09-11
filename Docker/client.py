import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(("localhost", 8888))

while(True):
    try:
        message = input("Enter message: ")
        s.sendall(message.encode())
        data = s.recv(1024)
        print(f"Received: {data.decode()}")
    except Exception as e: 
        print(f"Error: {e}")
        break