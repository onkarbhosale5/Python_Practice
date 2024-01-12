command = ""
isStarted = False
while True:
    command = input(">").upper()
    if command == "HELP":
        print("""
Start : to start the car
Stop : to stop the car
Quit : to exit""")
    elif command == "START":
        if isStarted:
            print("Car already started...")
        else:
            print("Car started. Ready to go...")
            isStarted = True
    elif command == "STOP":
        if not isStarted:
            print("Car already Stopped...")
        else:
            print("Car Stopped...")
            isStarted = False
    elif command == "QUIT":
        break
    else:
        print("I dont understand that")
