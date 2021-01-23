#output based on user input command
ip = ""
started = False
#stop = True
while True:
    ip = input("> ").lower()       
    if ip == "start" :
        if not started:
            print("started")
            started = True
        else:
            print ("already started")
    elif ip == "stop" :
        if started:
            print("stopped")
            started = False
        else:
            print ("already stopped")

    elif (ip=="help"):
        print("start")
        print("stop")
        print("quit")   

    elif (ip == "quit"):
        break
    else:
        print("wrong input")
        




