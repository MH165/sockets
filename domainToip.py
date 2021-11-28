import socket
"""Program to get the ip address for host on the internet"""
values = dict()
print("Enter q or Q to quit!")
while (True):
    try:
        hostname = input("Host: ")
        if (hostname=='q' or hostname=='Q'):
            break
        else:
            ip = socket.gethostbyname(hostname) 
            values.update({hostname:ip})
        
    except KeyboardInterrupt:
        print("Type error")
for key,value in values.items():
    print(f"The ip address for {key} is {value}")
print("\nThanks For Using Our Tool")
        
