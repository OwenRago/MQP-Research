import socket

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("0.0.0.0", 8888))
except socket.error as err:
    print(f"socket error: {err}")

s.listen(10)

while True:
    
    client_socket, client_address = s.accept()


    # Echo the received data back to the client
    while True:
        echo = client_socket.recv(1024)
        if not echo:
            break
        client_socket.sendall(echo)
        print(f"Echoed: {echo.decode()}")
    
    client_socket.close()
