import socket

HOST = '0.0.0.0'
PORT = 5002

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    while True:
        conn, addr = s.accept()
        with conn:
            print(f"connected by {addr}")
            data = conn.recv(1024)
            if data:
                response = (
                    "HTTP/1.1 200 OK\r\n"
                    "Content-Type: text/plain\r\n"
                    "Content-Lenght: 16\r\n"
                    "\r\n"
                    "PONG"
                    )
                conn.sendall(response.encode())
