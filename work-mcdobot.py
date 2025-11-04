print("Hi! I am McDoBot, a bot that assists your order!")
fries = "phd"
main = input("What main dish do you want? ")

while fries.lower() != "no" and fries.lower() != "yes":
    fries = str(input("Do you want fries with your meal? "))
    if fries.lower() == "yes":
        print(f"Sure! Here is your {main} with fries!")
    elif fries.lower() == "no":
        print(f"Sure! Here is your {main} with no fries!")
    else:
        print(f"I don't know what you mean by '{fries}', would you enter again?")
