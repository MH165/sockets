import socket
IP_ADDRESS = '127.0.0.1'
PORT_NUMBER = 9999
connection = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
connection.bind((IP_ADDRESS,PORT_NUMBER))
connection.listen()
client,address = connection.accept()
print(f"connection from {address}")
isClose = False
while not isClose:
    msg = client.recv(2048).decode()
    print(msg)
    if(msg=="quit"):
        break
client.close()
