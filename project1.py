import random

subjects = [
    "Shahrukh Khan",
    "Virat Kohli",
    "Nirmala Sitharaman",
    "A Mumbai Cat",
    "A Group of Monkeys",
    "Prime Minister Modi",
    "Auto Rickshaw Driver from Delhi"
]

actions = [
    "launches",
    "cancels",
    "dances with",
    "eats",
    "declares war on",
    "orders",
    "celebrates"
]

places_or_things = [
    "at red Fort",
    "in Mumbai Local Train",
    "a plate of samosa",
    "inside parliament",
    "at Ganga Ghat",
    "during IPL Match",
    "at India Gate"
]

while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    places_or_thing = random.choice(places_or_things)

    headline = f"Breaking News: {subject} {action} {places_or_thing}"

    print('\n' + headline)

    user_input = input(
        "\nDo you want another headline? (yes/no)").strip().lower()
    if user_input == "no":
        break


print("\nThanks for using the Fake News Heaadline Generator. have a fun day")
