
command=""
while True:
    command= input(">").lower()
    if command == "start":
       print('car started')
    elif command == "stop":
       print('car stopped')
    elif command == "help":
        print('''  
        start means to start a car
        stop means to stop a car
        quit means to quit the game   
        ''')
    elif command == "quit":
        print('quit game')
        break
    else:
        print("Sorry I don't understand it")