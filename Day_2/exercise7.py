#The Car Game
x=0
started = False
#Instructions
while x<1:
    user_input = input("> ").upper()
    if user_input == "HELP":
        print("""
start - To start the Car.
stop - To stop the car.
quit - To exit
""")
    elif user_input == "START":
        #This line checks to make sure start is not repeated twice
        if started:
            print("HeY!! You have already started the car")
        else:
            print("Car Started")
    elif user_input == "STOP":
        print("Car stopped")
    elif user_input == "QUIT":
        break
    else:
        print("I dont Understand that")