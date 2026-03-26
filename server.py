import socket
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(("10.10.3.28",9999))
while(True):
    msg=input("enter any")
    client.send(msg.encode())
    msg1=client.recv(1024).decode()
    print("server:",msg1)