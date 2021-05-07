import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = '0.0.0.0'
port = 1024


server.bind((ip, port))
server.listen(5)

client, address = server.accept()

print("IP:",address[0])
print("PORTA:",address[1])

while True:
    izy = client.recv(1024)
    print("message of the client: ",izy.decode())
    client.send(("RECEIVED ").encode())

    server.close()
