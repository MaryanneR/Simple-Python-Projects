# Print Greeting
print("Welcome to the Love Calculator!")

# Get name input from user
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

# Convert names to lowercase and concatenate
both_names = (name1 + name2).lower()

# Count TRUE
t_num = both_names.count("t")
r_num = both_names.count("r")
u_num = both_names.count("u")
e_num = both_names.count("e")

true_val = t_num + r_num + u_num + e_num

# Count LOVE
l_num = both_names.count("l")
o_num = both_names.count("o")
v_num = both_names.count("v")
e_num = both_names.count("e")

love_val = l_num + o_num + v_num + e_num

# TRUE LOVE Value
score = str(true_val) + str(love_val)
score = int(score)

# Score Interpretation
if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score > 40 and score < 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")