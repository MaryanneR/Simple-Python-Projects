import random

# Greeting
print("Welcome to Banker Roulette.\nTime to decide which of you pays the bill.")

# Get name input
names_string = input("Give me everybody's names, separated by a comma.\n")
names = names_string.split(", ")

# Pick random name
random_person = random.choice(names)

# Return name
print(f"{random_person} is going to buy the meal today!")