import socket

# Initial account balance
balance = 1000.0

def handle_transaction(command):
    global balance
    parts = command.split()
    if len(parts) == 0:
        return "Invalid command."

    action = parts[0].lower()
    if action == "deposit" and len(parts) == 2:
        try:
            amount = float(parts[1])
            balance += amount
            return f"Deposited {amount}. New balance: {balance}"
        except:
            return "Invalid amount."
    elif action == "withdraw" and len(parts) == 2:
        try:
            amount = float(parts[1])
            if amount > balance:
                return "Insufficient funds."
            balance -= amount
            return f"Withdrew {amount}. New balance: {balance}"
        except:
            return "Invalid amount."
    elif action == "balance":
        return f"Current balance: {balance}"
    else:
        return "Invalid command. Use: deposit <amount>, withdraw <amount>, balance"

# Server setup
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 12345))
server.listen(5)
print("Server listening on port 12345...")

while True:
    conn, addr = server.accept()
    print(f"Connected by {addr}")
    conn.send(b"Welcome! Use: deposit <amount>, withdraw <amount>, balance\n")
    while True:
        try:
            data = conn.recv(1024).decode().strip()
            if not data:
                break
            response = handle_transaction(data)
            conn.send(response.encode())
        except ConnectionResetError:
            break
    conn.close()
    print(f"Connection closed: {addr}")
