# While Loop 
# ==================

# This is used to execute a block of codes multiple times. It is also useful for writing interactive programs

# The Syntax 

# While <condition> :
#     <...block of code>
#     <an incremental value> {NB this line code prevents the loop statement from looping forever. so it is very much needed}

# example
# x=1
# while x<5:
#     print(x)
#     x=x+1

# Exercise
# ================
# Write a program using [while loop] that will request a user to guess a secret number. The user only has 3 options.
# print you have won if the user ia able to guess the secret number correctly or You have failed if the user is not
# able to guess the secret number after the 3rd attempt

secret_number = 10
guess_count =0
guess_limit = 3

while guess_count<guess_limit:
   user_number= int(input("Enter a secret number"))
   guess_count = guess_count + 1
   if user_number == 10:
      print("You have a won")
      break
else:("You have failed all attempts")