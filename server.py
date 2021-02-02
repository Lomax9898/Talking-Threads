# Rural Young N01132160
# Kevin Lomax n01120755

import socket

#Initialization
s = socket.socket()
print("Socket initialized")

port = int(input("Please input the port you are testing on: "))

try:
    s.bind(('', port))
    print("Socket was successfully bound to " + str(port))
except Exception as e:
    print(e)

s.listen(5)
print("Socket is listening")

while True:
    c, addr = s.accept()
    print("incoming connection from " + str(addr))

    msg = 'Connection was successful!'
    c.send(msg.encode())

    c.close()