# Rural Young N01132160
# Kevin Lomax n01120755

import socket

s = socket.socket()

port = int(input("Please input the port you are testing on: "))

s.connect(("139.62.210.153", port))

print(s.recv(1024) )

s.close()
