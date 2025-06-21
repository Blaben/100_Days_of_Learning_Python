# Write a program about a buyer who wants to buy a house of price $1M
# if the buyer has a good credit, they need to put down %10
# otherwiise, they need to put down 20%. print down the statement

price = 1000000
buyer = True
downpay = 0

if buyer:
    downpay = price*0.1
    print(f"You can make a down payment of {downpay}")
    print("You have a good credit")

else:
    downpay = price*0.2
    print(f"You have to make a down payment of {downpay}")
    print("you have a bad credit")