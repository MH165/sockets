import socket
IP_ADDRESS = '127.0.0.1'
PORT_NUMBER = 9999
connection = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
connection.connect((IP_ADDRESS,PORT_NUMBER))
try:
    while(True):
        USER = input()
        connection.send(USER.encode())
        if USER =="quit":
            break
        
except KeyboardInterrupt:
    print("Bye...")

connection.close()