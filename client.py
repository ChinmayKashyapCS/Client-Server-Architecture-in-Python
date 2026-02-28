import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 12345))

# Receive welcome message
print(client.recv(1024).decode())

while True:
    command = input("Enter command (deposit/withdraw/balance or 'exit'): ")
    if command.lower() == "exit":
        break
    client.send(command.encode())
    response = client.recv(1024).decode()
    print("Server:", response)

client.close()
