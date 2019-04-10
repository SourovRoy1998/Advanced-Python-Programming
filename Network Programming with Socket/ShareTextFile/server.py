import socket
address=("0.0.0.0",5000)
soc = socket.socket()
soc.bind(address)
print("Server is running...")
soc.listen(1)
conn, add = soc.accept()




while True:
    data = conn.recv(1024).decode('utf-8')
    with open(data,"r") as f:
        data = f.read()
        conn.send(data.encode('utf-8'))
    
conn.close()
