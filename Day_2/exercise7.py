#The Car Game
started = False #this line checks the status of the car
print("Enter start to see the list of available options ")
#Instructions
while True: #this condition is set to make the loop run infinitely
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
            print("Hey!! You have already started the car")
        else:
            started = True
            print("Car Started..")
    
    elif user_input == "STOP":
        if not started:
            print("Hey! you have already stopped the car..")

        else:
            started = False
            print("Car stopped")

    elif user_input == "QUIT":
        break
    else:
        print("I dont Understand that")