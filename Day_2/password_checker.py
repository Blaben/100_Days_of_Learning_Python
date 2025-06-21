# """ Question : Password Checker
# Problem:
# Write a program that keeps asking the user to enter a password until they enter the correct one.
# The correct password is "opensesame""""

while True:
    user_input = input("Enter your Password ")

    if user_input == "opensesame":
        print("Login Successful..")
        break
    else:
        print("Wrong Password, Try again")
        