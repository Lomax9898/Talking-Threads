# Rural Young n01132160
# Kevin Lomax n01120755

import socket
import subprocess
import threading

# defining functions used
def bindPort(socket, port):
    try:
        socket.bind(('', port))
        print("Socket was successfully bound to " + str(port))
    except Exception as e:
        port = int(input("Error! Invalid or busy port! Please input a valid port to test on: "))
        bindPort(s, port)

# Essentially a switch statement
def switch(case):
    if case == '1':
        #est = time.asctime( time.localtime(time.time()) )
        test = subprocess.check_output("date", shell=True, universal_newlines=True)
        c.send(str(test).encode())
        print("Sent Data")
    elif case == '2':
        test = subprocess.check_output('uptime', shell=True,universal_newlines=True)
        c.send(str(test).encode())
        print("Sent Data")
    elif case == '3':
        test = subprocess.check_output('free', shell=True, universal_newlines=True)
        c.send(str(test).encode())
        print("Sent Data")
    elif case == '4':
        test = subprocess.check_output('netstat', shell=True,universal_newlines=True)
        c.send(str(test).encode())
        print("Sent Data")
    elif case == '5':
        test = subprocess.check_output('users', shell=True, universal_newlines=True)
        c.send(str(test).encode())
        print("Sent Data")
    elif case == '6':
        test = subprocess.check_output('ps -U root -u root -N', shell=True, universal_newlines=True)
        c.send(str(test).encode())
        print("Sent Data")

def talkingThreads(c):
    while True:
        try:
            choice = c.recv(1024)
            if choice:
                result = choice.decode("utf-8")
                switch(result)
            else:
                error = "Timeout Error"
                c.send(error.encode())
        except:
            c.close()
            return False


# Initialization
s = socket.socket()
print("Socket initialized")

# Binding the port
inputPort = int(input("Please input the port you are testing on: "))
bindPort(s, inputPort)

# Listening in for connections
s.listen(5)
print("Socket is listening")


# When receiving incoming connections
while True:
    c, addr = s.accept()
    c.settimeout(30)
    print("incoming connection from " + str(addr))
    print("Received data...")
    threading.Thread(target=talkingThreads, args=(c,)).start()
    print("...and sent data")

s.close()
