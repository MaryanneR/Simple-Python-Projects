# Greeting
print("Welcome to Skull Mountain! Here is where you'll get your ticket for the rollercoaster.\
\nLet's check your height first to see if you're tall enough for the Skull Mountain experience.")

# Get height input from user
height = int(input("What is your height in cm?: "))

# Get age to determine base ticket price
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("How old are you? "))
    if age < 12:
        print("Child tickets are $5")
        bill = 5
    elif age <= 18:
        print("Youth tickets are $7")
        bill = 7
    else:
        print("Adult tickets are $12")
        bill = 12

    # Ask whether they want a photo for an additional cost
    wants_photo = input("Do you want a photo taken? It'll be $3 extra. Y or N: ")
    if wants_photo == 'Y':
        print("Awesome! Make sure to strike a cool/funny pose!")
        bill += 3

    # Return final bill
    print(f"Your final bill is ${bill}. Happy riding!")

else:
    print("Sorry, you're a little too small to ride the rollercoaster. Maybe next time.")
