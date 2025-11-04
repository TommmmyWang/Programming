# function to print "hello"
def say_hello():
    print("Hello!")


say_hello()


# function to print a personalized hello
def say_hello_nicely(name: str):
    print(f"hello {name}!")


say_hello_nicely("steve")


def normalize_input(user_input: str):
    # Takes user input and cleans it up.
    output = user_input.lower().strip(",.?!")
    return output


def normalized_input():
    # Takes user input and cleans it up.
    output = input().lower().strip(",.?!")
    return output


print(normalize_input("rainy!!"))
print(normalize_input("YES!!!!!!"))

# Ask the user that the weather is
weather_reply = normalized_input()
