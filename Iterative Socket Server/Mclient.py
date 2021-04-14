# Rural Young n01132160
# Kevin Lomax n01120755
import threading
import socket
import time

Restart = True

# Initializing which port we're going to be testing on.
while True:
    try:
        port = int(input("Please input the port you are testing on: "))
        if int(port) > 1025 and int(port) < 4998:
            break
        else:
            print("The input should be a port between 1025-4998")
    except ValueError:
        print("Provide an integer value...")
        continue

# Inputting the net address
netaddress = input("Please input the network address you are testing on: ")
while Restart == True:
    print("\nOperations:")
    print(
        " 1 - Date and Time, the date and time on the server \n 2 - Uptime, how long the server has been running since "
        "boot up \n "
        "3 - Memory Use, the current memory usage on the server \n 4 - Netstat, lists network connections on the "
        "server "
        "\n "
        "5 - Current Users, list of users current running on the server \n 6 - Running Processes, list of programs "
        "running on the server")

    # Asking which operation to perform
    while True:
        try:
            op = input("Please enter a number of the operation you want to perform: ")
            if int(op) > 0 and int(op) < 7:
                break
            else:
                print("The input should be a number between 1-6")
        except ValueError:
            print("Provide an integer value...")
            continue

    # Asking how many times you want that operation to perform
    while True:
        try:
            clients = int(input("How many clients do you want to generate? "))
            if clients > 0 and clients < 101:
                break
            else:
                print("The input should be a reasonable number")
        except ValueError:
            print("Provide an integer value...")
            continue


    # This is the instructions for each thread to carry out
    def Cread(times_list):
        c = socket.socket()
        c.connect((netaddress, port))
        time_start = time.perf_counter()
        c.send(bytes(op, "utf-8"))
        serverdata = c.recv(1024)
        time_end = time.perf_counter()
        print('______________________________________________________________________________________________')
        print('Received from the server :', serverdata.decode("ascii"))
        elapsed_time = time_end - time_start
        times_list.append(elapsed_time)
        print("Client", threading.currentThread().getName(), "took", str(round(elapsed_time, 4)), "seconds")
        c.close()


    thread_times = []

    # start threads by passing function and list to Thread constructor
    for i in range(clients):
        t = threading.Thread(target=Cread, args=(thread_times,))
        t.start()
        t.join()

    # Stops the following code from exectuing before the threads all finish their tasks
    while len(thread_times) != clients:
        time.sleep(1)

    # Further time calculations for each thread
    total_time = sum(float(i) for i in thread_times)
    avg_time = total_time / clients

    # Time calculates are printed
    print('______________________________________________________________________________________________')
    print("The Total Turn-around Time:", str(round(total_time, 4)), "seconds")
    print("The Average Turn-around Time:", str(round(avg_time, 4)), "seconds")

    # Confirmation on seeing the turnaround times for each thread
    view_times = input("Would you like to view turn-around Time (elapsed time) for each client request?(yes/no) ")
    if view_times == "yes":
        print(thread_times)

    # Asking if you would like to restart
    restart = input("Would you like to do more operations?(yes/no) ")
    if restart == "no":
        restart = False
        exit()
