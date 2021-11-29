import socket

"""This simple program can not get banner of some services 
you can try using nmap  """

well_known_port = [443,80,21,22,23,53,445,139,25,110]
IP = int(input("Enter ip address: "))
# YOU CAN USE IT FOR SCAN LOCALHOST OR WHATEVER
for PORT in well_known_port:
    try:
        connection = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        connection.settimeout(20)
        connection.connect((IP,PORT))
        service_version = connection.recv(1024).decode()

        print(f"{PORT} {service_version}")
    except TimeoutError:
        print("It is look like the port are closed !")
        continue
connection.close()
    