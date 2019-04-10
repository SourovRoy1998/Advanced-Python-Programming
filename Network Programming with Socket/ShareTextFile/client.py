import socket
host="192.168.31.170"
port=5000
soc = socket.socket()
soc.connect((host,port))

while True:
    print("================================")
    print("Which text file do you want?")
    data = input("Enter name with extension: ")
    print("================================")
    if data=="exit":
        break
    soc.send(data.encode('utf-8'))
    with open(data,"w+") as f:
        data=soc.recv(4098).decode('utf-8')
        print(data)
        f.write(data)
    

