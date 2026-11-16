import socket

host = "127.0.0.1"
puertos = range(1, 1025)

for puerto in puertos:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(0.3)
        if s.connect_ex((host, puerto)) == 0:
            print(f"Puerto {puerto} abierto")