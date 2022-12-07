# Simple tip calculator

# Program Greeting
print("Welcome to the tip calculator.")

# Get input
bill = float(input("Please enter your bill amount: $"))
tip = int(input("How much would you like to tip? 10, 12, or 15? (don't type percent sign) "))
people = int(input("How many people are splitting the bill? "))

# Calculate each person's amount to pay
total_bill = bill + (tip / 100 * bill)
amount_to_pay = round(total_bill / people, 2)

# Show amount_to_pay
print(f"Each person should pay : ${amount_to_pay}")


