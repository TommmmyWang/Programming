def create_mood_message(name="Person", mood="neutral"):
    name = input("What is your name?")
    mood = input("How are you feeling today?")
    if mood.lower().strip(",.?!") == "happy" or mood.lower().strip(",.?!") == "good":
        print(f"Hey {name}, great to see you smiling!")
    elif mood.lower().strip(",.?!") == "sad" or mood.lower().strip(",.?!") == "bad":
        print(f"I hope your day gets better, {name}.")
    elif mood.lower().strip(",.?!") == "neutral":
        print(f"Sometimes you have average days, {name}.")
    else:
        print(f"Hi {name}, hope you're having a good day.")


def average(num1, num2, num3):
    """Return the Average of the Three given Numbers"""
    return float((num1 + num2 + num3) / 3)


average(50, 53.1, 56)

create_mood_message()
