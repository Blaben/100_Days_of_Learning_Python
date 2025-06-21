# """ Question : Password Checker
# Problem:
# Write a program that keeps asking the user to enter a password until they enter the correct one the user has 3 options only after block the user.
# The correct password is "opensesame""""

i = 0
while i<3:
    user_input = input("Enter your Password ")
    i = i + 1 #same as i+=1

    if user_input == "opensesame":
        print("Login Successful..")
        break
    elif i<3:
        print("Wrong Password, Try again")
else:
    print("You have entered the incorrect password so many times. Try again in 10 minutes")

#herrrr the code be sweet wai lol